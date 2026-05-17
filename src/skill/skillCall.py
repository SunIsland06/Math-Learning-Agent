"""
技能调用器模块 —— 负责将 LLM 的工具调用请求路由到对应的技能实现。

工作机制：
1. SkillManager 从 skill/ 目录自动发现所有技能
2. build_tools() 生成 OpenAI 兼容的工具定义列表
3. execute_tool_call() 解析工具调用参数，动态加载 Python 入口并执行
4. 支持 Python 模块入口（skill_entry/run/main/handle）和二进制入口
"""

from __future__ import annotations

import base64
import importlib.util
import inspect
import json
import re
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional

from skill.skillManager import SkillManager, SkillSpec


_TOOL_CALL_FUNC = "function"


def merge_tool_call_delta(tool_calls: List[Dict[str, Any]], delta_calls: List[Dict[str, Any]]) -> None:
    """将流式返回的工具调用增量合并成完整的工具调用列表。

    DeepSeek API 的流式工具调用会跨多个 SSE chunk 返回，
    每个 chunk 只包含部分字段（id/name/arguments），需要累积合并。

    Args:
        tool_calls: 目标列表（原地修改），累积完整的工具调用
        delta_calls: 当前 chunk 中的增量工具调用数据
    """
    for call in delta_calls:
        index = int(call.get("index", 0))
        # 补齐列表长度
        while len(tool_calls) <= index:
            tool_calls.append({"id": "", "type": _TOOL_CALL_FUNC, "function": {"name": "", "arguments": ""}})

        target = tool_calls[index]
        if call.get("id"):
            target["id"] = call["id"]
        if call.get("type"):
            target["type"] = call["type"]

        func_delta = call.get("function", {})
        if "name" in func_delta and func_delta["name"]:
            target["function"]["name"] = func_delta["name"]
        if "arguments" in func_delta and func_delta["arguments"]:
            target["function"]["arguments"] += func_delta["arguments"]


class SkillCaller:
    """技能调用器 —— 管理技能生命周期并提供统一的工具调用接口。

    Attributes:
        manager: SkillManager 实例，负责技能发现与元数据管理
        context: 注入到每次技能调用的全局上下文（如 output_dir）
    """

    def __init__(self, skill_root: Optional[Path] = None) -> None:
        """初始化技能调用器并自动加载所有技能。

        Args:
            skill_root: 技能目录路径，默认为仓库根目录的 skill/
        """
        self.manager = SkillManager(skill_root=skill_root)
        self.manager.load_skills()
        self.context: Dict[str, Any] = {}

    def build_tools(self) -> List[Dict[str, Any]]:
        """生成供 LLM 使用的 OpenAI 格式工具定义列表。"""
        return [spec.to_openai_tool() for spec in self.manager.skills.values()]

    def execute_tool_call(self, name: str, arguments: str) -> str:
        """解析工具调用参数并执行对应技能。

        Args:
            name: 工具名称（对应 SKILL.md 中的 name 字段）
            arguments: JSON 格式的参数字符串

        Returns:
            技能执行结果字符串。
        """
        payload = self._parse_arguments(arguments)
        # 注入全局上下文（如 output_dir），已存在的键不覆盖
        if self.context:
            params = payload.get("params")
            if isinstance(params, dict):
                for key, value in self.context.items():
                    params.setdefault(key, value)
                payload["params"] = params
            else:
                payload["params"] = {"value": params, **self.context}

        spec = self.manager.get_skill(name)
        if not spec:
            return f"Skill not found: {name}"

        return self._execute_skill(spec, payload)

    def build_tool_message(self, tool_call_id: str, name: str, result: str) -> Dict[str, Any]:
        """构建 OpenAI 格式的 tool 角色消息。

        Args:
            tool_call_id: 工具调用 ID（由 LLM 生成）
            name: 工具名称
            result: 工具执行结果

        Returns:
            tool 角色消息字典。
        """
        return {
            "role": "tool",
            "tool_call_id": tool_call_id,
            "name": name,
            "content": result,
        }

    # ============================================================
    # 参数解析
    # ============================================================

    def _parse_arguments(self, arguments: str) -> Dict[str, Any]:
        """解析 LLM 传来的工具参数，兼容 JSON 与纯文本两种格式。

        Returns:
            {"input": str, "params": dict} 格式的标准化载荷。
        """
        if not arguments:
            return {"input": "", "params": {}}

        try:
            data = json.loads(arguments)
        except json.JSONDecodeError:
            # 非 JSON 字符串直接视为 input
            return {"input": arguments, "params": {}}

        if not isinstance(data, dict):
            return {"input": json.dumps(data, ensure_ascii=False), "params": {}}

        input_text = data.get("input", "")
        params = data.get("params", {})
        if not isinstance(params, dict):
            params = {"value": params}

        return {"input": input_text, "params": params}

    # ============================================================
    # 技能执行
    # ============================================================

    def _execute_skill(self, spec: SkillSpec, payload: Dict[str, Any]) -> str:
        """根据技能定义选择执行方式。

        优先尝试 entry_files（Python 或二进制），
        若无入口文件则回退到从 SKILL.md 正文中提取预期输出。

        Args:
            spec: 技能规格
            payload: 标准化载荷 {"input": ..., "params": ...}

        Returns:
            技能执行结果字符串。
        """
        if spec.entry_files:
            for entry in spec.entry_files:
                suffix = entry.suffix.lower()
                if suffix == ".py":
                    return self._run_python_entry(entry, payload)
                if suffix in {".exe", ".bin"}:
                    return self._run_binary_entry(entry, payload)

        # 回退：从指令文本中提取预期输出
        fallback = self._extract_expected_output(spec.instruction)
        return fallback or spec.description or spec.instruction or f"Skill {spec.name} executed."

    def _run_python_entry(self, path: Path, payload: Dict[str, Any]) -> str:
        """动态加载 Python 模块并调用入口函数。

        按优先级查找入口函数：skill_entry → run → main → handle。

        Args:
            path: Python 文件路径
            payload: 标准化载荷

        Returns:
            函数返回值（已规范化为字符串）。
        """
        module = self._load_module_from_path(path)
        if not module:
            return f"Failed to load python entry: {path.name}"

        for func_name in ("skill_entry", "run", "main", "handle"):
            func = getattr(module, func_name, None)
            if callable(func):
                return self._invoke_callable(func, payload)

        return f"No callable entry found in {path.name}"

    def _run_binary_entry(self, path: Path, payload: Dict[str, Any]) -> str:
        """以子进程方式执行二进制入口，通过 stdin 传递 JSON 参数。

        Args:
            path: 可执行文件路径
            payload: 标准化载荷

        Returns:
            进程 stdout 输出，无输出时返回 stderr。
        """
        try:
            proc = subprocess.run(
                [str(path)],
                input=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
        except Exception as exc:
            return f"Binary execution error: {exc}"

        stdout = proc.stdout.decode("utf-8", errors="ignore").strip()
        if stdout:
            return stdout

        stderr = proc.stderr.decode("utf-8", errors="ignore").strip()
        return stderr or "Binary executed with no output."

    # ============================================================
    # 模块加载
    # ============================================================

    def _load_module_from_path(self, path: Path):
        """从文件路径动态加载 Python 模块。

        Args:
            path: .py 文件路径

        Returns:
            加载的模块对象，失败返回 None。
        """
        try:
            spec = importlib.util.spec_from_file_location(path.stem, path)
            if not spec or not spec.loader:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None

    # ============================================================
    # 函数调用适配
    # ============================================================

    def _invoke_callable(self, func, payload: Dict[str, Any]) -> str:
        """根据函数签名智能选择调用方式。

        0 参数：func()
        1 参数：func(payload)
        2 参数：func(input, params)

        Args:
            func: 可调用对象
            payload: 标准化载荷 {"input": ..., "params": ...}

        Returns:
            函数返回值（已规范化为字符串）。
        """
        try:
            sig = inspect.signature(func)
            params = list(sig.parameters.values())
        except (TypeError, ValueError):
            params = []

        try:
            if len(params) == 0:
                result = func()
            elif len(params) == 1:
                result = func(payload)
            else:
                result = func(payload.get("input"), payload.get("params"))
        except Exception as exc:
            return f"Python execution error: {exc}"

        return self._normalize_result(result)

    # ============================================================
    # 结果规范化
    # ============================================================

    def _normalize_result(self, result: Any) -> str:
        """将各种类型的返回值统一转换为字符串。

        - None → ""
        - bytes → Base64 data URI
        - dict/list → JSON 字符串
        - 其他 → str()
        """
        if result is None:
            return ""
        if isinstance(result, bytes):
            return "data:application/octet-stream;base64," + base64.b64encode(result).decode("ascii")
        if isinstance(result, (dict, list)):
            return json.dumps(self._make_json_safe(result), ensure_ascii=False)
        return str(result)

    def _make_json_safe(self, value: Any) -> Any:
        """递归处理不可 JSON 序列化的值（如 bytes → Base64）。"""
        if isinstance(value, bytes):
            return "data:application/octet-stream;base64," + base64.b64encode(value).decode("ascii")
        if isinstance(value, list):
            return [self._make_json_safe(item) for item in value]
        if isinstance(value, dict):
            return {key: self._make_json_safe(val) for key, val in value.items()}
        return value

    def _extract_expected_output(self, instruction: str) -> str:
        """从技能指令文本中提取预期输出（引号内的内容）。

        取最后一个中文或英文引号内的文本作为回退输出。

        Args:
            instruction: SKILL.md 的正文内容

        Returns:
            提取的预期输出文本，无匹配时返回空字符串。
        """
        if not instruction:
            return ""

        matches = re.findall(r"[\"\"](.+?)[\"\"]", instruction)
        if matches:
            return matches[-1]

        return ""
