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
    for call in delta_calls:
        index = int(call.get("index", 0))
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
    def __init__(self, skill_root: Optional[Path] = None) -> None:
        self.manager = SkillManager(skill_root=skill_root)
        self.manager.load_skills()

    def build_tools(self) -> List[Dict[str, Any]]:
        return [spec.to_openai_tool() for spec in self.manager.skills.values()]

    def execute_tool_call(self, name: str, arguments: str) -> str:
        payload = self._parse_arguments(arguments)
        spec = self.manager.get_skill(name)
        if not spec:
            return f"Skill not found: {name}"

        return self._execute_skill(spec, payload)

    def build_tool_message(self, tool_call_id: str, name: str, result: str) -> Dict[str, Any]:
        return {
            "role": "tool",
            "tool_call_id": tool_call_id,
            "name": name,
            "content": result,
        }

    def _parse_arguments(self, arguments: str) -> Dict[str, Any]:
        if not arguments:
            return {"input": "", "params": {}}

        try:
            data = json.loads(arguments)
        except json.JSONDecodeError:
            return {"input": arguments, "params": {}}

        if not isinstance(data, dict):
            return {"input": json.dumps(data, ensure_ascii=False), "params": {}}

        input_text = data.get("input", "")
        params = data.get("params", {})
        if not isinstance(params, dict):
            params = {"value": params}

        return {"input": input_text, "params": params}

    def _execute_skill(self, spec: SkillSpec, payload: Dict[str, Any]) -> str:
        if spec.entry_files:
            for entry in spec.entry_files:
                suffix = entry.suffix.lower()
                if suffix == ".py":
                    return self._run_python_entry(entry, payload)
                if suffix in {".exe", ".bin"}:
                    return self._run_binary_entry(entry, payload)

        fallback = self._extract_expected_output(spec.instruction)
        return fallback or spec.description or spec.instruction or f"Skill {spec.name} executed."

    def _run_python_entry(self, path: Path, payload: Dict[str, Any]) -> str:
        module = self._load_module_from_path(path)
        if not module:
            return f"Failed to load python entry: {path.name}"

        for func_name in ("skill_entry", "run", "main", "handle"):
            func = getattr(module, func_name, None)
            if callable(func):
                return self._invoke_callable(func, payload)

        return f"No callable entry found in {path.name}"

    def _run_binary_entry(self, path: Path, payload: Dict[str, Any]) -> str:
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

    def _load_module_from_path(self, path: Path):
        try:
            spec = importlib.util.spec_from_file_location(path.stem, path)
            if not spec or not spec.loader:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None

    def _invoke_callable(self, func, payload: Dict[str, Any]) -> str:
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

    def _normalize_result(self, result: Any) -> str:
        if result is None:
            return ""
        if isinstance(result, bytes):
            return "data:application/octet-stream;base64," + base64.b64encode(result).decode("ascii")
        if isinstance(result, (dict, list)):
            return json.dumps(result, ensure_ascii=False)
        return str(result)

    def _extract_expected_output(self, instruction: str) -> str:
        if not instruction:
            return ""

        matches = re.findall(r"[\"“](.+?)[\"”]", instruction)
        if matches:
            return matches[-1]

        return ""
