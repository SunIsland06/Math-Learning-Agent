import requests

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from config.globalConfig import get_global_config

class Model:
    def __init__(self, model_name=None, system_prompt="你是一个乐于助人的助手"):
        config = get_global_config()
        self.api_key = config.key
        self.base_url = config.api_url
        self.model_name = model_name or config.model
        self.messages = [{"role": "system", "content": system_prompt}]

        if not self.api_key:
            raise ValueError("API key is empty in config/global.yml")
        if not self.base_url:
            raise ValueError("APIUrl is empty in config/global.yml")
        if not self.model_name:
            raise ValueError("model is empty in config/global.yml and no override was provided")

    def chat(self, user_text, temperature=0.7):
        self.messages.append({"role": "user", "content": user_text})

        payload = {
            "model": self.model_name,
            "messages": self.messages,
            "temperature": temperature,
            "stream": False
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        resp = requests.post(self.base_url, headers=headers, json=payload, timeout=60)
        data = resp.json()

        if resp.status_code != 200:
            raise RuntimeError(f"Request failed: {data}")

        assistant_reply = data["choices"][0]["message"]["content"]
        self.messages.append({"role": "assistant", "content": assistant_reply})
        return assistant_reply

    def reset(self, system_prompt=None):
        if system_prompt is None:
            system_prompt = self.messages[0]["content"] if self.messages else "你是一个乐于助人的助手"
        self.messages = [{"role": "system", "content": system_prompt}]