import requests
import json

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from config.globalConfig import get_global_config


class Model:

    # 初始化设置
    def __init__(
        self,
        model_name=None,
        system_prompt="你是一个帮助指导数学学习的助手。",
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
        self.messages = [{"role": "system", "content": system_prompt}]
    
    # 普通聊天接口
    def chat(self, prompt, temperature=0.7, extra_params=None):
        self.messages.append({"role": "user", "content": prompt})

        payload = {
            "model": self.model_name,
            "messages": self.messages,
            "temperature": temperature,
        }
        
        if extra_params:
            payload.update(extra_params)
            
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        try:
            res = requests.post(self.base_url, 
                                json=payload, 
                                headers=headers, 
                                timeout=self.timeout)
            res.raise_for_status()
            
            answer = res.json()["choices"][0]["message"]["content"]
            self.messages.append({"role": "assistant", "content": answer})
            return answer
        except Exception as e:
            error_msg = f"Model request error: {str(e)}"
            return error_msg
    
    # 流式传输接口
    
    def stream_chat(self, prompt, temperature=0.7, extra_params=None):
        """流式返回助手回复的生成器，每次 yield 一个内容片段 (str)

        Args:
            prompt (_type_): 提示词
            temperature (float, optional): 温度参数. Defaults to 0.7.
            extra_params (_type_, optional): 额外参数. Defaults to None.
        """
        
        self.messages.append({"role": "user", "content": prompt})

        payload = {
            "model": self.model_name,
            "messages": self.messages,
            "temperature": temperature,
            "stream": True
        }
        
        if extra_params:
            payload.update(extra_params)
            
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        try:
            res = requests.post(
                self.base_url, 
                json=payload, 
                headers=headers, 
                timeout=self.timeout, 
                stream=True
            )
            res.raise_for_status()
            
            full_answer = "" # 用于拼接完整回答
            
            # 逐行读取流式响应
            for line in res.iter_lines(decode_unicode=True):
                if not line:
                    continue
                if line.startswith("data: "):
                    data_str = line[6:]
                    if data_str == "[DONE]":
                        break
                    try:
                        chunk = json.loads(data_str)
                        delta = chunk["choices"][0].get("delta", {})
                        content = delta.get("content", "")
                        if content:
                            full_answer += content
                            # 逐字产出
                            for char in content:
                                yield char
                    except (json.JSONDecodeError, KeyError, IndexError):
                        continue
            
            self.messages.append({"role": "assistant", "content": full_answer})
        except Exception as e:
            error_msg = f"Model request error: {str(e)}"
            yield error_msg
    
    # 重置对话
    def reset(self):
        self.messages = [self.messages[0]]  # 保留系统提示，清除用户和助手的对话记录