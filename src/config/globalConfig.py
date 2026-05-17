"""
全局配置管理模块 —— 以单例模式加载 config/global.yml 配置文件。

配置文件格式（YAML）：
    APIUrl: https://api.deepseek.com/v1/chat/completions
    key: sk-xxxx
    model: deepseek-chat
    search: false
    memory: false

使用方式：
    from config.globalConfig import get_global_config
    cfg = get_global_config()
    print(cfg.api_url, cfg.model)
"""

import os
import yaml


class GlobalConfig:
    """全局配置单例 —— 从 config/global.yml 读取并缓存配置。

    通过 __new__ 实现线程安全的单例模式，
    __init__ 通过 _initialized 标志确保仅初始化一次。
    """

    _instance = None
    _initialized = False

    def __new__(cls):
        """单例创建 —— 仅首次调用时实例化。"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """初始化配置属性 —— 仅首次调用时从 YAML 文件加载。

        后续实例化会跳过 __init__ 逻辑，避免重复读取文件。
        """
        if self.__class__._initialized:
            return
        self.__class__._initialized = True

        config_path = self._resolve_config_path()
        data = self._load_yaml(config_path)

        # 从 YAML 提取配置项并设置默认值
        self.api_url = self._get_str(data, "APIUrl")
        self.key = self._get_str(data, "key")
        self.model = self._get_str(data, "model")
        self.search = bool(data.get("search", False))
        self.memory = bool(data.get("memory", False))
        self.wolfram_app_id = self._get_str(data, "wolfram_app_id")

    def _resolve_config_path(self):
        """解析配置文件路径 —— 仓库根目录/config/global.yml。"""
        repo_root = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        return os.path.join(repo_root, "config", "global.yml")

    def _load_yaml(self, path):
        """加载 YAML 配置文件，文件不存在时返回空字典。"""
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}

    def _get_str(self, data, key):
        """安全获取字符串配置项，None 值转为空字符串。"""
        value = data.get(key, "")
        if value is None:
            return ""
        return str(value).strip()


def get_global_config():
    """获取 GlobalConfig 单例实例（推荐使用此函数而非直接实例化）。"""
    return GlobalConfig()
