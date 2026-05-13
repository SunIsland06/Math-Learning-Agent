import os
import requests

class Model:
    def __init__(self, model_name="deepseek-chat", system_prompt="你是一个乐于助人的助手"):
        self.api_key = self._load_key()
        self.base_url = "https://api.deepseek.com/chat/completions"
        self.model_name = model_name
        self.messages = [{"role": "system", "content": system_prompt}]

    def _load_key(self):
        # API.txt is in the same folder as this file
        dir_path = os.path.dirname(os.path.abspath(__file__))
        api_path = os.path.join(dir_path, "API.txt")
        with open(api_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("KEY:"):
                    return line.split("KEY:", 1)[1].strip()
        raise ValueError("KEY not found in API.txt")

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