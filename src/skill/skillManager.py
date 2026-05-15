from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re
from typing import Dict, List, Optional, Tuple


_FRONT_MATTER_BOUNDARY = "---"


@dataclass
class SkillSpec:
	name: str
	description: str
	folder_path: Path
	skill_file: Path
	instruction: str
	secondary_files: List[Path] = field(default_factory=list)
	entry_files: List[Path] = field(default_factory=list)

	def to_anthropic_tool(self) -> Dict:
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
	def __init__(self, skill_root: Optional[Path] = None) -> None:
		repo_root = Path(__file__).resolve().parents[2]
		self.skill_root = skill_root or (repo_root / "skill")
		self.skills: Dict[str, SkillSpec] = {}

	def load_skills(self) -> Dict[str, SkillSpec]:
		self.skills = {}
		if not self.skill_root.exists() or not self.skill_root.is_dir():
			return self.skills

		for child in self.skill_root.iterdir():
			if not child.is_dir():
				continue

			skill_file = child / "SKILL.md"
			if not skill_file.exists():
				continue

			meta, body = self._parse_front_matter(skill_file.read_text(encoding="utf-8"))
			name = (meta.get("name") or "").strip()
			if not name or name != child.name:
				continue

			description = (meta.get("description") or "").strip()
			instruction, secondary_files = self._apply_secondary_indices(body, child)
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
		if not self.skills:
			self.load_skills()
		return self.skills.get(name)

	def get_anthropic_tools(self) -> List[Dict]:
		if not self.skills:
			self.load_skills()
		return [spec.to_anthropic_tool() for spec in self.skills.values()]

	def build_skill_catalog(self) -> str:
		if not self.skills:
			self.load_skills()

		lines: List[str] = []
		for spec in self.skills.values():
			lines.append(f"- {spec.name}: {spec.description}")
		return "\n".join(lines)

	def _parse_front_matter(self, text: str) -> Tuple[Dict[str, str], str]:
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
		matches = []
		for pattern in [r"调用[\s:：]*[\"“](.+?\.md)[\"”]", r"《(.+?\.md)》"]:
			matches.extend(re.findall(pattern, text))

		return list(dict.fromkeys(matches))

	def _find_entry_files(self, text: str, base_dir: Path) -> List[Path]:
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