"""
用户个人配置管理 —— 读取/写入 userdata/<username>/config.yml。
"""
import os
from pathlib import Path
from typing import Any, Dict

import yaml

# 默认配置
DEFAULT_CONFIG: Dict[str, Any] = {
    "thinking": "enabled",
    "thinking_strength": "high",
    "search": False,
    "memory": False,
}

USERDATA_ROOT = Path(__file__).resolve().parents[2] / "userdata"


def _config_path(username: str) -> Path:
    safe = _sanitize(username)
    return USERDATA_ROOT / safe / "config.yml"


def _sanitize(name: str) -> str:
    """防止路径穿越。"""
    return "".join(c for c in name if c.isalnum() or c in "-_.") or "unknown"


def load_config(username: str) -> Dict[str, Any]:
    """加载用户配置，不存在则返回默认值。"""
    path = _config_path(username)
    if not path.exists():
        return dict(DEFAULT_CONFIG)
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
    except Exception:
        return dict(DEFAULT_CONFIG)
    # 合并默认值，填补缺失项
    merged = dict(DEFAULT_CONFIG)
    merged.update({k: v for k, v in data.items() if k in DEFAULT_CONFIG})
    return merged


def save_config(username: str, config: Dict[str, Any]) -> bool:
    """保存用户配置。只保存 DEFAULT_CONFIG 中存在的键。"""
    path = _config_path(username)
    path.parent.mkdir(parents=True, exist_ok=True)
    filtered = {k: v for k, v in config.items() if k in DEFAULT_CONFIG}
    try:
        with open(path, "w", encoding="utf-8") as f:
            yaml.safe_dump(filtered, f, allow_unicode=True, default_flow_style=False)
        return True
    except Exception:
        return False
