"""
技能管理器模块 —— 从 skill/ 目录自动发现和加载技能定义。

工作原理：
1. 扫描 skill/ 下的每个子目录
2. 解析 SKILL.md 的 YAML front matter 获取 name/description
3. 解析正文中的入口文件引用（"调用: xxx.py"）
4. 生成 OpenAI / Anthropic 兼容的工具定义

技能目录结构示例：
    skill/
      geometry/
        SKILL.md          ← 技能元数据 + 使用说明
        geometry.py        ← 入口文件（可选）
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re
from typing import Dict, List, Optional, Tuple


_FRONT_MATTER_BOUNDARY = "---"


@dataclass
class SkillSpec:
    """技能规格 —— 描述一个技能的完整元数据。

    Attributes:
        name: 技能名称（须与目录名一致）
        description: 技能描述（简短说明）
        folder_path: 技能目录路径
        skill_file: SKILL.md 文件路径
        instruction: 合并后的技能使用说明（正文 + 二级索引）
        secondary_files: 二级索引引用的 .md 文件列表
        entry_files: 入口文件列表（.py / .exe / .bin）
    """
    name: str
    description: str
    folder_path: Path
    skill_file: Path
    instruction: str
    secondary_files: List[Path] = field(default_factory=list)
    entry_files: List[Path] = field(default_factory=list)

    def to_anthropic_tool(self) -> Dict:
        """生成 Anthropic Messages API 格式的工具定义。"""
        description = self.description or f"Skill {self.name}."
        if self.instruction:
            description = f"{description}\n\nUsage:\n{self.instruction}"

        return {
            "name": self.name,
            "description": description,
            "input_schema": {
                "type": "object",
                "properties": {
                    "input": {
                        "type": "string",
                        "description": "User request or parameters for this skill.",
                    },
                    "params": {
                        "type": "object",
                        "description": "Optional structured parameters.",
                    },
                },
                "required": ["input"],
            },
        }

    def to_openai_tool(self) -> Dict:
        """生成 OpenAI / DeepSeek API 兼容的工具定义。

        每个工具接受两个参数：
        - input: 用户请求或参数（必填）
        - params: 结构化可选参数（如 output_dir, task 等）
        """
        description = self.description or f"Skill {self.name}."
        if self.instruction:
            description = f"{description}\n\nUsage:\n{self.instruction}"

        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": description,
                "parameters": {
                    "type": "object",
                    "properties": {
                        "input": {
                            "type": "string",
                            "description": "User request or parameters for this skill.",
                        },
                        "params": {
                            "type": "object",
                            "description": "Optional structured parameters.",
                        },
                    },
                    "required": ["input"],
                },
            },
        }


class SkillManager:
    """技能管理器 —— 扫描 skill/ 目录，解析 SKILL.md 并构建技能元数据。

    单次扫描成本低，可在每次请求时重新加载以获取最新技能。
    """

    def __init__(self, skill_root: Optional[Path] = None) -> None:
        """初始化技能管理器。

        Args:
            skill_root: 技能根目录，默认为仓库根目录下的 skill/
        """
        repo_root = Path(__file__).resolve().parents[2]
        self.skill_root = skill_root or (repo_root / "skill")
        self.skills: Dict[str, SkillSpec] = {}

    def load_skills(self) -> Dict[str, SkillSpec]:
        """扫描技能目录，解析所有 SKILL.md 并构建 SkillSpec。

        遍历 skill_root 下的每个子目录：
        1. 查找 SKILL.md 文件
        2. 解析 YAML front matter 获取 name/description
        3. 解析正文中的入口文件引用
        4. 合并二级索引内容

        Returns:
            技能名 → SkillSpec 的映射字典。
        """
        self.skills = {}
        if not self.skill_root.exists() or not self.skill_root.is_dir():
            return self.skills

        for child in self.skill_root.iterdir():
            if not child.is_dir():
                continue

            skill_file = child / "SKILL.md"
            if not skill_file.exists():
                continue

            # 解析 YAML front matter
            meta, body = self._parse_front_matter(skill_file.read_text(encoding="utf-8"))
            name = (meta.get("name") or "").strip()
            # name 必须与目录名一致
            if not name or name != child.name:
                continue

            description = (meta.get("description") or "").strip()
            # 合并二级索引 .md 文件内容
            instruction, secondary_files = self._apply_secondary_indices(body, child)
            # 查找入口文件（.py/.exe/.bin）
            entry_files = self._find_entry_files(body, child)

            self.skills[name] = SkillSpec(
                name=name,
                description=description,
                folder_path=child,
                skill_file=skill_file,
                instruction=instruction,
                secondary_files=secondary_files,
                entry_files=entry_files,
            )

        return self.skills

    def get_skill(self, name: str) -> Optional[SkillSpec]:
        """按名称获取技能规格。未加载时自动加载。

        Args:
            name: 技能名称

        Returns:
            SkillSpec 或 None（技能不存在时）。
        """
        if not self.skills:
            self.load_skills()
        return self.skills.get(name)

    def get_anthropic_tools(self) -> List[Dict]:
        """生成 Anthropic 格式的完整工具清单。"""
        if not self.skills:
            self.load_skills()
        return [spec.to_anthropic_tool() for spec in self.skills.values()]

    def build_skill_catalog(self) -> str:
        """生成技能目录文本（用于展示可用技能列表）。"""
        if not self.skills:
            self.load_skills()

        lines: List[str] = []
        for spec in self.skills.values():
            lines.append(f"- {spec.name}: {spec.description}")
        return "\n".join(lines)

    # ============================================================
    # SKILL.md 解析
    # ============================================================

    def _parse_front_matter(self, text: str) -> Tuple[Dict[str, str], str]:
        """解析 SKILL.md 的 YAML front matter。

        front matter 格式：
        ---
        name: geometry
        description: 绘制 2D/3D 函数图像
        ---
        正文内容...

        Args:
            text: SKILL.md 文件全文

        Returns:
            (元数据字典, 正文字符串)。
        """
        text = text.lstrip()
        if not text.startswith(_FRONT_MATTER_BOUNDARY):
            return {}, text.strip()

        parts = text.split(_FRONT_MATTER_BOUNDARY, 2)
        if len(parts) < 3:
            return {}, text.strip()

        _, meta_block, body = parts
        meta: Dict[str, str] = {}
        for line in meta_block.splitlines():
            line = line.strip()
            if not line or ":" not in line:
                continue
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip().strip('"').strip("'")

        return meta, body.strip()

    def _apply_secondary_indices(self, body: str, base_dir: Path) -> Tuple[str, List[Path]]:
        """将正文中引用的二级索引 .md 文件内容合并进技能说明。

        引用格式："调用: xxx.md" 或 "《xxx.md》"

        Args:
            body: SKILL.md 正文
            base_dir: 技能目录路径

        Returns:
            (合并后的完整指令文本, 二级文件路径列表)。
        """
        secondary_files: List[Path] = []
        extra_parts: List[str] = []

        for filename in self._find_secondary_files(body):
            candidate = (base_dir / filename).resolve()
            if not candidate.exists() or not candidate.is_file():
                continue

            content = candidate.read_text(encoding="utf-8").strip()
            _, content_body = self._parse_front_matter(content)
            if content_body:
                extra_parts.append(f"[Secondary Index: {candidate.name}]\n{content_body}")
                secondary_files.append(candidate)

        merged = body.strip()
        if extra_parts:
            merged = f"{merged}\n\n" + "\n\n".join(extra_parts)

        return merged, secondary_files

    def _find_secondary_files(self, text: str) -> List[str]:
        """从正文中提取二级索引文件名（去重保持顺序）。

        Args:
            text: SKILL.md 正文

        Returns:
            去重后的 .md 文件名列表。
        """
        matches = []
        for pattern in [r"调用[\s:：]*[\"\"](.+?\.md)[\"\"]", r"《(.+?\.md)》"]:
            matches.extend(re.findall(pattern, text))

        return list(dict.fromkeys(matches))

    def _find_entry_files(self, text: str, base_dir: Path) -> List[Path]:
        """从正文中查找技能入口文件（Python 或二进制）。

        引用格式："调用: geometry.py"

        Args:
            text: SKILL.md 正文
            base_dir: 技能目录路径

        Returns:
            存在的入口文件路径列表。
        """
        entries: List[Path] = []
        pattern = r"调用[\s:：]*([^\s，。；;]+?\.(?:py|exe|bin))"
        for match in re.findall(pattern, text):
            candidate = (base_dir / match).resolve()
            if candidate.exists():
                entries.append(candidate)

        return entries


if __name__ == "__main__":
    manager = SkillManager()
    skills = manager.load_skills()

    for name, spec in skills.items():
        print(f"Loaded skill: {name} - {spec.description}")
