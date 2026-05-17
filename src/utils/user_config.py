"""
用户个人配置管理模块 —— 读写 userdata/<username>/config.yml。

每个用户拥有独立的配置文件，存储功能开关偏好：
- thinking: 是否启用深度思考（"enabled" / "disabled"）
- thinking_strength: 思考强度（"high" / "low"）
- search: 是否启用联网搜索（bool）
- memory: 是否启用长期记忆（bool）

使用方式：
    from utils.user_config import load_config, save_config
    cfg = load_config("username")
    save_config("username", {"search": True})
"""

import os
from pathlib import Path
from typing import Any, Dict

import yaml

# 默认配置 —— 新用户的初始设置
DEFAULT_CONFIG: Dict[str, Any] = {
    "thinking": "enabled",
    "thinking_strength": "high",
    "search": False,
    "memory": False,
}

USERDATA_ROOT = Path(__file__).resolve().parents[2] / "userdata"


def _sanitize(name: str) -> str:
    """过滤用户名中的非法字符，防止路径穿越攻击。"""
    return "".join(c for c in name if c.isalnum() or c in "-_.") or "unknown"


def _config_path(username: str) -> Path:
    """获取用户配置文件的绝对路径。"""
    safe = _sanitize(username)
    return USERDATA_ROOT / safe / "config.yml"


def load_config(username: str) -> Dict[str, Any]:
    """加载用户配置，不存在的键自动填充默认值。

    Args:
        username: 用户名

    Returns:
        合并默认值后的配置字典。
    """
    path = _config_path(username)
    if not path.exists():
        return dict(DEFAULT_CONFIG)
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
    except Exception:
        return dict(DEFAULT_CONFIG)
    # 合并默认值，确保所有键都存在
    merged = dict(DEFAULT_CONFIG)
    merged.update({k: v for k, v in data.items() if k in DEFAULT_CONFIG})
    return merged


def save_config(username: str, config: Dict[str, Any]) -> bool:
    """保存用户配置 —— 仅存储 DEFAULT_CONFIG 中定义的键，过滤未知字段。

    Args:
        username: 用户名
        config: 待保存的配置字典

    Returns:
        True 表示保存成功，False 表示失败。
    """
    path = _config_path(username)
    path.parent.mkdir(parents=True, exist_ok=True)
    filtered = {k: v for k, v in config.items() if k in DEFAULT_CONFIG}
    try:
        with open(path, "w", encoding="utf-8") as f:
            yaml.safe_dump(filtered, f, allow_unicode=True, default_flow_style=False)
        return True
    except Exception:
        return False
