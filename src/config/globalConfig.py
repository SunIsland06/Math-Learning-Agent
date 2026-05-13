import os

import yaml

# 读取全局配置，单例模式
class GlobalConfig:
	_instance = None
	_initialized = False

	def __new__(cls):
		if cls._instance is None:
			cls._instance = super().__new__(cls)
		return cls._instance

	def __init__(self):
		if self.__class__._initialized:
			return
		self.__class__._initialized = True

		config_path = self._resolve_config_path()
		data = self._load_yaml(config_path)

		self.api_url = self._get_str(data, "APIUrl")
		self.key = self._get_str(data, "key")
		self.model = self._get_str(data, "model")
		self.search = bool(data.get("search", False))
		self.memory = bool(data.get("memory", False))

	def _resolve_config_path(self):
		repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
		return os.path.join(repo_root, "config", "myglobal.yml")

	def _load_yaml(self, path):
		with open(path, "r", encoding="utf-8") as f:
			return yaml.safe_load(f) or {}

	def _get_str(self, data, key):
		value = data.get(key, "")
		if value is None:
			return ""
			
		return str(value).strip()


def get_global_config():
	return GlobalConfig()
