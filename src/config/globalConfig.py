import os

import yaml

# 读取全局配置，单例模式
class GlobalConfig:
	_instance = None
	_initialized = False

	def __new__(cls):
		# 单例创建
		if cls._instance is None:
			cls._instance = super().__new__(cls)
		return cls._instance

	def __init__(self):
		# 避免重复初始化
		if self.__class__._initialized:
			return
		self.__class__._initialized = True

		# 读取配置文件并填充属性
		config_path = self._resolve_config_path()
		data = self._load_yaml(config_path)

		self.api_url = self._get_str(data, "APIUrl")
		self.key = self._get_str(data, "key")
		self.model = self._get_str(data, "model")
		self.search = bool(data.get("search", False))
		self.memory = bool(data.get("memory", False))

	def _resolve_config_path(self):
		# 配置文件位于仓库根目录的 config/global.yml
		repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
		return os.path.join(repo_root, "config", "global.yml")

	def _load_yaml(self, path):
		# 加载 YAML 配置
		with open(path, "r", encoding="utf-8") as f:
			return yaml.safe_load(f) or {}

	def _get_str(self, data, key):
		# 获取字符串配置并做清理
		value = data.get(key, "")
		if value is None:
			return ""
			
		return str(value).strip()


def get_global_config():
	return GlobalConfig()
