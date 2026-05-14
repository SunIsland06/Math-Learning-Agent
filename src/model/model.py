import json
import requests

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from config.globalConfig import get_global_config


class Model:
    def __init__(
        self,
        model_name=None,
        system_prompt=None,
        api_key=None,
        base_url=None,
        default_stream=None,
        timeout=60,
    ):
        config = get_global_config()
        self.api_key = api_key or config.key
        self.base_url = base_url or config.api_url
        self.model_name = model_name or config.model
        self.default_stream = (
            default_stream if default_stream is not None else getattr(config, "stream", None)
        )
        self.timeout = timeout

        self.system_prompt = system_prompt or load_system_prompt()
        self.messages = [{"role": "system", "content": self.system_prompt}]
    
    def stream_chat_chunks(self, prompt, temperature=0.7, extra_params=None):
        """Yield model output by content chunk."""
        self.messages.append({"role": "user", "content": prompt})

        payload = {
            "model": self.model_name,
            "messages": self.messages,
            "temperature": temperature,
            "stream": True,
        }
        if extra_params:
            payload.update(extra_params)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        try:
            res = requests.post(
                self.base_url,
                json=payload,
                headers=headers,
                timeout=self.timeout,
                stream=True,
            )
            res.raise_for_status()

            full_answer = ""
            for line in res.iter_lines(decode_unicode=True):
                if not line or not line.startswith("data: "):
                    continue

                data_str = line[6:]
                if data_str == "[DONE]":
                    break

                try:
                    chunk = json.loads(data_str)
                    delta = chunk["choices"][0].get("delta", {})
                    content = delta.get("content", "")
                except (json.JSONDecodeError, KeyError, IndexError):
                    continue

                if content:
                    full_answer += content
                    yield content

            self.messages.append({"role": "assistant", "content": full_answer})
        except Exception as e:
            yield f"Model request error: {str(e)}"

    def stream_chat(self, prompt, temperature=0.7, extra_params=None):
        """Backward compatible char-level stream."""
        for chunk in self.stream_chat_chunks(prompt, temperature=temperature, extra_params=extra_params):
            for char in chunk:
                yield char

    def reset(self):
        self.messages = [self.messages[0]]


def load_system_prompt():
    prompt_path = Path(__file__).parent.parent / "prompt" / "system.md"
    return prompt_path.read_text(encoding="utf-8").strip()


if __name__ == "__main__":
    model = Model()
    print(model.system_prompt)
