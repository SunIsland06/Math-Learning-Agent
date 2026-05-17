"""
Wolfram Alpha 查询技能 —— 通过 Wolfram Alpha API 进行复杂数学计算和公式推导。

支持两种 API 模式：
1. Short Answers API (v1/result) — 返回纯文本结果，适合简单查询
2. Full Results API (v2/query) — 返回结构化结果（含图片、分类信息等），适合复杂查询

配置方式：在 config/global.yml 中设置 wolfram_app_id 字段

获取 App ID：https://developer.wolframalpha.com/

入口函数：skill_entry(payload) → str
"""

import json
import sys
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
from pathlib import Path

# 从全局配置读取 Wolfram Alpha App ID
_WOLFRAM_APP_ID = None


def _get_app_id() -> str:
    """延迟加载 Wolfram Alpha App ID（从全局配置读取）。"""
    global _WOLFRAM_APP_ID
    if _WOLFRAM_APP_ID is not None:
        return _WOLFRAM_APP_ID

    try:
        sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
        from config.globalConfig import get_global_config
        cfg = get_global_config()
        _WOLFRAM_APP_ID = getattr(cfg, "wolfram_app_id", "") or ""
    except Exception:
        _WOLFRAM_APP_ID = ""
    return _WOLFRAM_APP_ID


def _wolfram_short_answer(query: str) -> str:
    """调用 Wolfram Alpha Short Answers API (v1)。

    返回简短的纯文本结果，适合计算类查询（如 "derivative of x^2"）。

    Args:
        query: 数学查询字符串

    Returns:
        API 返回的文本结果或错误提示。
    """
    app_id = _get_app_id()
    if not app_id:
        return "Wolfram Alpha API 未配置 App ID。请在 config/global.yml 中设置 wolfram_app_id。"

    base_url = "https://api.wolframalpha.com/v1/result"
    params = urllib.parse.urlencode({
        "appid": app_id,
        "i": query,
        "units": "metric",
    })

    try:
        url = f"{base_url}?{params}"
        req = urllib.request.Request(url, headers={"User-Agent": "Math-Learning-Agent/1.0"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            result = resp.read().decode("utf-8")
            return _format_short_result(query, result)
    except urllib.error.HTTPError as e:
        return _handle_http_error(e, query)
    except Exception as e:
        return f"Wolfram Alpha 查询异常: {e}"


def _wolfram_full_query(query: str) -> str:
    """调用 Wolfram Alpha Full Results API (v2/query)。

    返回结构化结果，包含多个 pod（输入解释、结果、图表、分类等）。
    自动提取关键 pod：Input interpretation、Results、Plot、Alternate forms 等。

    Args:
        query: 数学查询字符串

    Returns:
        格式化的 Markdown 结果文本。
    """
    app_id = _get_app_id()
    if not app_id:
        return "Wolfram Alpha API 未配置 App ID。请在 config/global.yml 中设置 wolfram_app_id。"

    base_url = "https://api.wolframalpha.com/v2/query"
    params = urllib.parse.urlencode({
        "appid": app_id,
        "input": query,
        "format": "image,plaintext",
        "output": "json",
        "units": "metric",
    })

    try:
        url = f"{base_url}?{params}"
        req = urllib.request.Request(url, headers={"User-Agent": "Math-Learning-Agent/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return _format_full_result(query, data)
    except urllib.error.HTTPError as e:
        # 若 Full Results API 失败则回退到 Short Answer
        if e.code in (403, 401):
            return _handle_http_error(e, query)
        return _wolfram_short_answer(query)
    except Exception as e:
        return f"Wolfram Alpha 查询异常: {e}"


def _format_short_result(query: str, result: str) -> str:
    """格式化 Short Answers API 结果。"""
    return (
        f"【Wolfram Alpha 计算结果】\n\n"
        f"查询: `{query}`\n\n"
        f"结果: **{result}**\n"
    )


def _format_full_result(query: str, data: dict) -> str:
    """格式化 Full Results API 的 JSON 返回数据。

    提取关键信息 pod：
    - Input interpretation: 输入解析
    - Result/Derivative/Integral 等：主要结果
    - Plot/Image: 图表
    - Alternate forms: 等价表达式
    - Number line: 数轴

    Args:
        query: 原始查询字符串
        data: Wolfram Alpha Full Results API 返回的 JSON

    Returns:
        Markdown 格式的精美结果。
    """
    queryresult = data.get("queryresult", {})
    if not queryresult.get("success", False):
        # 尝试获取错误信息
        error_msg = queryresult.get("error", {})
        if isinstance(error_msg, dict):
            msg = error_msg.get("msg", "Wolfram Alpha 无法理解此查询")
        else:
            msg = str(error_msg) if error_msg else "Wolfram Alpha 无法理解此查询"
        tips = queryresult.get("tips", {})
        tip_text = ""
        if isinstance(tips, dict):
            tip_text = tips.get("text", "")
        return (
            f"【Wolfram Alpha 查询提示】\n\n"
            f"查询: `{query}`\n\n"
            f"{msg}\n\n"
            f"{'建议: ' + tip_text if tip_text else ''}\n\n"
            f"提示：请尝试用英文数学表达式重新表述，或使用 symbolic_computation 工具进行符号计算。"
        )

    pods = queryresult.get("pods", [])
    parts = [f"【Wolfram Alpha 完整结果】\n"]
    parts.append(f"查询: `{query}`\n")

    # 按优先级提取 pod
    image_urls = []

    for pod in pods:
        title = pod.get("title", "")
        subpods = pod.get("subpods", [])

        if not subpods:
            continue

        # 输入解析
        if title in ("Input", "Input interpretation"):
            plaintext = subpods[0].get("plaintext", "")
            if plaintext:
                parts.append(f"### 输入解析\n{plaintext}\n")

        # 主要结果
        elif title in ("Result", "Derivative", "Integral", "Limit", "Series expansion",
                       "Exact result", "Decimal approximation", "Solutions", "Solution"):
            for sp in subpods:
                plaintext = sp.get("plaintext", "")
                if plaintext:
                    # 尝试使用 LaTeX 包装数学表达式
                    formatted = _try_latex_wrap(plaintext)
                    parts.append(f"### {title}\n{formatted}\n")

                # 提取图片
                img = sp.get("img", {})
                if isinstance(img, dict) and img.get("src"):
                    image_urls.append((title, img["src"]))

        # 图表
        elif title in ("Plot", "Plots", "3DPlot", "Contour plot", "Number line"):
            for sp in subpods:
                img = sp.get("img", {})
                if isinstance(img, dict) and img.get("src"):
                    image_urls.append((title, img["src"]))
                plaintext = sp.get("plaintext", "")
                if plaintext:
                    parts.append(f"### {title}\n{plaintext}\n")

        # 等价形式
        elif title in ("Alternate forms", "Alternate form", "Expanded form",
                       "Simplified form", "Factored form"):
            for sp in subpods:
                plaintext = sp.get("plaintext", "")
                if plaintext:
                    parts.append(f"### {title}\n{_try_latex_wrap(plaintext)}\n")

        # 其他有用信息
        elif title in ("Number name", "Continued fraction", "Series representations",
                       "Definite integral", "Indefinite integral", "Root",
                       "Properties", "Period"):
            for sp in subpods:
                plaintext = sp.get("plaintext", "")
                if plaintext:
                    parts.append(f"### {title}\n{plaintext}\n")

    # 添加图片
    if image_urls:
        parts.append("### 图表\n")
        for title, url in image_urls[:4]:  # 最多4张图
            parts.append(f"![{title}]({url})\n")

    if len(parts) == 2:  # 只有标题+查询，没有结果
        # 回退：提取所有 pod 的 plaintext
        for pod in pods:
            title = pod.get("title", "")
            for sp in pod.get("subpods", []):
                plaintext = sp.get("plaintext", "")
                if plaintext and title:
                    parts.append(f"### {title}\n{plaintext}\n")

    parts.append(f"\n> 由 Wolfram Alpha 提供技术支持")
    return "\n".join(parts)


def _try_latex_wrap(text: str) -> str:
    """尝试将数学表达式用 LaTeX 包装，增强可读性。

    对包含特殊数学符号的结果自动添加行内数学格式 $$...$$。
    """
    if not text:
        return text
    # 检测是否包含数学符号
    math_symbols = ["^", "_", "\\", "∫", "∑", "√", "∂", "∞", "π", "θ", "±"]
    has_math = any(s in text for s in math_symbols)
    if has_math:
        # 如果文本中有行内公式，尝试用 $$ 包装
        if len(text) < 60 and "\n" not in text:
            return f"$$\n{text}\n$$"
    return text


def _handle_http_error(error: urllib.error.HTTPError, query: str) -> str:
    """统一处理 Wolfram Alpha HTTP 错误。"""
    if error.code == 403 or error.code == 401:
        return (
            "Wolfram Alpha API 认证失败。\n"
            "请检查 config/global.yml 中的 wolfram_app_id 是否正确。\n"
            "获取免费 App ID: https://developer.wolframalpha.com/\n\n"
            "替代方案：使用 symbolic_computation 工具进行符号计算。"
        )
    if error.code == 501:
        return (
            f"Wolfram Alpha 无法理解该查询：「{query}」\n"
            "建议：\n"
            "1. 尝试用英文表达式重新表述\n"
            "2. 使用 symbolic_computation 工具进行符号计算"
        )
    return f"Wolfram Alpha 查询失败 (HTTP {error.code}): {error.reason}"


def skill_entry(payload: dict) -> str:
    """技能入口 —— 执行 Wolfram Alpha 查询并返回格式化结果。

    当 App ID 未配置时，自动引导用户使用 symbolic_computation 工具。

    Args:
        payload: {
            "input": str (查询文本),
            "params": {
                "query": str,    # Wolfram Alpha 查询内容
                "mode": str,     # "short" (Short Answers) 或 "full" (Full Results，默认)
            }
        }

    Returns:
        格式化的 Markdown 结果文本。
    """
    payload = payload or {}
    params = payload.get("params") or {}
    query = params.get("query") or payload.get("input", "")
    mode = params.get("mode", "full")

    if not query or not query.strip():
        return "错误：请提供 Wolfram Alpha 查询内容。"

    query = query.strip()

    # 未配置 App ID 时的友好提示
    app_id = _get_app_id()
    if not app_id:
        return (
            "【Wolfram Alpha 未配置】\n\n"
            "Wolfram Alpha App ID 尚未设置。如需使用此功能，请：\n\n"
            "1. 访问 https://developer.wolframalpha.com/ 注册并获取免费 App ID\n"
            "2. 在 config/global.yml 中设置 `wolfram_app_id: 你的AppID`\n"
            "3. 重启应用\n\n"
            "**替代方案**：您可以使用 symbolic_computation 工具进行符号计算，"
            "它支持求导、积分、极限、方程求解、矩阵运算等功能，且无需额外配置。"
        )

    if mode == "short":
        return _wolfram_short_answer(query)
    return _wolfram_full_query(query)
