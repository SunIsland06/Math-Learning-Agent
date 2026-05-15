import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import io
import base64
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