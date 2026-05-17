"""
Wolfram Alpha Skill —— 通过 Wolfram Alpha API 查询复杂数学计算结果。
"""
import json
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET


# Wolfram Alpha App ID —— 使用免费/演示 key
_WOLFRAM_APP_ID = None  # 如需使用，在此填入 App ID


def _wolfram_query(query: str) -> str:
    """向 Wolfram Alpha Short Answers API 发起查询。"""
    if not _WOLFRAM_APP_ID:
        return (
            "Wolfram Alpha API 未配置。请设置 App ID。\n"
            "替代方案：使用 symbolic_computation 工具进行符号计算。"
        )

    base_url = "https://api.wolframalpha.com/v1/result"
    params = urllib.parse.urlencode({
        "appid": _WOLFRAM_APP_ID,
        "i": query,
        "units": "metric",
    })

    try:
        url = f"{base_url}?{params}"
        req = urllib.request.Request(url, headers={"User-Agent": "Math-Learning-Agent/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = resp.read().decode("utf-8")
            return f"【Wolfram Alpha 结果】\n查询: {query}\n结果: {result}"
    except urllib.error.HTTPError as e:
        if e.code == 403:
            return f"Wolfram Alpha API 认证失败，请检查 App ID。"
        if e.code == 501:
            return f"Wolfram Alpha 无法理解该查询：「{query}」，请尝试用英文表达式重新表述。"
        return f"Wolfram Alpha 查询失败 (HTTP {e.code}): {e.reason}"
    except Exception as e:
        return f"Wolfram Alpha 查询异常: {e}"


def skill_entry(payload: dict) -> str:
    """执行 Wolfram Alpha 查询。"""
    payload = payload or {}
    params = payload.get("params") or {}
    query = params.get("query") or payload.get("input", "")

    if not query or not query.strip():
        return "错误：请提供 Wolfram Alpha 查询内容。"

    return _wolfram_query(query.strip())
