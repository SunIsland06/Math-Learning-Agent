---
name: geometry_plotter
description: 在需要函数图像时，调用 geometry.py 生成 2D/3D 函数图，并返回 PNG 或 base64 数据。
---

# geometry 技能说明（DeepSeek 调用）

## 1. 技能用途
当 Agent 需要“结合函数图像进行讲解/验证/对比”时，调用本技能：
- 输入函数表达式与区间参数
- 生成函数图像（2D 或 3D）
- 返回 PNG 字节或 base64 图像数据

代码文件：`skill/geometry/geometry.py`
核心类：`GeometryGenerator`

## 2. 可调用函数

### 2.1 二维函数图（主功能）
函数：`generate_function_plot(expr: str, x_range=(-10, 10), title="") -> bytes`

说明：
- `expr`：关于 `x` 的表达式，例如 `np.sin(x)`、`x**2+2*x+1`
- `x_range`：横轴区间，如 `(-6, 6)`
- `title`：图标题，可留空

返回：PNG 图片字节（`bytes`)

### 2.2 三维曲面图
函数：`generate_3d_plot(expr: str, x_range=(-5,5), y_range=(-5,5), resolution=50) -> bytes`

说明：
- `expr`：关于 `x,y` 的表达式，例如 `np.sin(x)*np.cos(y)`
- `resolution`：网格密度，越大越精细也越耗时

返回：PNG 图片字节（`bytes`）

### 2.3 几何文字卡片（可选）
函数：`generate_geometry_description(description: str) -> bytes`

说明：将一段几何说明文本渲染成图片。

### 2.4 图片编码
函数：`plot_to_base64(plot_bytes: bytes) -> str`

返回：`data:image/png;base64,...`

## 3. DeepSeek 推荐调用流程
```python
from skill.geometry.geometry import GeometryGenerator

def run_plot2d(expr, x_range=(-10, 10), title=""):
    g = GeometryGenerator()
    img_bytes = g.generate_function_plot(expr=expr, x_range=x_range, title=title)
    img_b64 = g.plot_to_base64(img_bytes)
    return {
        "mime": "image/png",
        "image_bytes": img_bytes,
        "image_base64": img_b64,
        "used_params": {
            "task": "plot2d",
            "expr": expr,
            "x_range": x_range,
            "title": title,
        },
    }
```

## 4. 任务到参数映射
- `task=plot2d`
  - 必填：`expr`
  - 可选：`x_range`, `title`
- `task=plot3d`
  - 必填：`expr`
  - 可选：`x_range`, `y_range`, `resolution`
- `task=text_card`
  - 必填：`description`

## 5. 表达式规范
建议使用 NumPy 风格：
- 2D：`x**2`, `np.sin(x)`, `np.exp(-x**2)`
- 3D：`x*y`, `np.sin(x)*np.cos(y)`, `np.sqrt(x**2+y**2)`

禁止传入非数学代码（如导入语句、系统命令、文件操作等）。

## 6. 异常与回退
- 2D：先数值计算，失败后尝试 SymPy；仍失败则输出错误提示图。
- 3D：表达式失败时回退为零曲面图。

## 7. Agent 输出要求
每次返回图像时建议同时返回：
1. 图像本体（`image_bytes` 或 `image_base64`）
2. 本次使用参数（`used_params`）
3. 一句简短说明（画了什么函数、区间是什么）
