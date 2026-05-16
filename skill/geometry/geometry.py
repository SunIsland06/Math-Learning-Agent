import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import io
import base64
from pathlib import Path
from datetime import datetime
import numpy as np


class GeometryGenerator:
    def generate_function_plot(self, expr: str, x_range=(-10, 10), title="") -> bytes:
        x_vals = np.linspace(x_range[0], x_range[1], 400)
        try:
            y_vals = [eval(expr, {"x": v, "np": np}) for v in x_vals]
        except Exception:
            y_vals = None

        fig, ax = plt.subplots(figsize=(6, 4))
        if y_vals is not None:
            ax.plot(x_vals, y_vals)
        else:
            from sympy import symbols, plot
            x = symbols("x")
            try:
                sym_expr = eval(expr, {"x": x, **vars(__import__("sympy"))})
                p = plot(sym_expr, (x, x_range[0], x_range[1]), show=False)
                fig = p._backend.fig
            except Exception:
                ax.text(0.5, 0.5, f"无法解析: {expr}", ha="center", va="center", transform=ax.transAxes)
        ax.set_title(title or expr)
        ax.grid(True)

        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=150)
        plt.close(fig)
        buf.seek(0)
        return buf.getvalue()

    def generate_3d_plot(self, expr: str, x_range=(-5, 5), y_range=(-5, 5), resolution=50) -> bytes:
        x_vals = np.linspace(x_range[0], x_range[1], resolution)
        y_vals = np.linspace(y_range[0], y_range[1], resolution)
        X, Y = np.meshgrid(x_vals, y_vals)

        try:
            Z = eval(expr, {"x": X, "y": Y, "np": np})
            if hasattr(Z, "__iter__") and not isinstance(Z, np.ndarray):
                Z = np.array(Z)
        except Exception:
            Z = np.zeros_like(X)

        fig = plt.figure(figsize=(6, 5))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap="viridis")
        ax.set_title(expr)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")

        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=150)
        plt.close(fig)
        buf.seek(0)
        return buf.getvalue()

    def generate_geometry_description(self, description: str) -> bytes:
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.set_aspect("equal")
        ax.text(0.5, 0.5, description, ha="center", va="center", fontsize=14)
        ax.axis("off")
        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=150, bbox_inches="tight")
        plt.close(fig)
        buf.seek(0)
        return buf.getvalue()

    def plot_to_base64(self, plot_bytes: bytes) -> str:
        return "data:image/png;base64," + base64.b64encode(plot_bytes).decode()


def skill_entry(payload: dict) -> dict:
    """Skill entry for tool calls. Expects payload with keys: input, params."""
    payload = payload or {}
    params = payload.get("params") or {}
    task = (params.get("task") or "").strip() or "plot2d"
    generator = GeometryGenerator()
    output_dir = params.get("output_dir")
    output_url_prefix = params.get("output_url_prefix")

    def persist_image(image_bytes: bytes, prefix: str) -> dict:
        if not output_dir:
            return {
                "mime": "image/png",
                "image_bytes": image_bytes,
                "image_base64": generator.plot_to_base64(image_bytes),
            }

        folder = Path(str(output_dir))
        folder.mkdir(parents=True, exist_ok=True)
        filename = f"{prefix}-{datetime.utcnow().strftime('%Y%m%d%H%M%S%f')}.png"
        target = folder / filename
        target.write_bytes(image_bytes)
        url = f"{output_url_prefix or ''}{filename}"
        return {
            "mime": "image/png",
            "image_url": url,
            "image_path": str(target),
        }

    if task == "plot3d":
        expr = params.get("expr") or payload.get("input") or "0"
        x_range = params.get("x_range", (-5, 5))
        y_range = params.get("y_range", (-5, 5))
        resolution = params.get("resolution", 50)
        img_bytes = generator.generate_3d_plot(expr, x_range=x_range, y_range=y_range, resolution=resolution)
        image_info = persist_image(img_bytes, "plot3d")
        return {
            **image_info,
            "used_params": {
                "task": "plot3d",
                "expr": expr,
                "x_range": x_range,
                "y_range": y_range,
                "resolution": resolution,
            },
            "summary": f"3D plot for {expr}",
        }

    if task == "text_card":
        description = params.get("description") or payload.get("input") or ""
        img_bytes = generator.generate_geometry_description(description)
        image_info = persist_image(img_bytes, "text")
        return {
            **image_info,
            "used_params": {
                "task": "text_card",
                "description": description,
            },
            "summary": "Text card rendered",
        }

    expr = params.get("expr") or payload.get("input") or "x"
    x_range = params.get("x_range", (-10, 10))
    title = params.get("title", "")
    img_bytes = generator.generate_function_plot(expr, x_range=x_range, title=title)
    image_info = persist_image(img_bytes, "plot2d")
    return {
        **image_info,
        "used_params": {
            "task": "plot2d",
            "expr": expr,
            "x_range": x_range,
            "title": title,
        },
        "summary": f"2D plot for {expr}",
    }