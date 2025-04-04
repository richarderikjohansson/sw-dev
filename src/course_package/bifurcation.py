import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def logistic_equation(x: float, r: float) -> float:
    """Calculates the logistic equation


    Args:
        x: Seed for the logistic equation
        r: Anchor for the logistic equation

    Returns:
        Updated seed
    """
    xn = r * x * (1 - x)
    return xn


def make_logistic_map(points: int, iterations: int) -> tuple:
    """Updates the map

    Args:
        points: number of points for the seed and anchor
        iterations: Number of times the map should be updated

    Returns:
        Updated values for the anchor and seed
    """
    r = np.linspace(0, 4, points)
    x = np.random.rand(points)
    for _ in range(iterations):
        x = logistic_equation(x, r)

    return r, x


def plot_map(points: int, iterations: int) -> None:
    """Plotting the logistic map

    Args:
        points: Numbers of points for the seed and anchor
        iterations: Number of times the map should be updated
    """
    r, x = make_logistic_map(points=points, iterations=iterations)
    equation = r"$x_{n+1} = rx_{n}(1-x_{n})$, "
    counter = f"for n={iterations}"

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.plot(r, x, ls="", marker=",", color="black", alpha=0.1, label=equation + counter)
    ax.set_xlim(-0.1, 4.1)
    ax.set_ylim(-0.05, 1.05)
    ax.set_xlabel("$r$", fontsize=15)
    ax.set_ylabel(r"$x_n$", fontsize=15)
    ax.legend(loc="upper left", frameon=False)
    ax.spines[["right", "top"]].set_visible(False)
    fig.savefig("logistic_map_plot.png", dpi=200)


def animate_map(points: int, iterations: int) -> None:
    """Animate the logistic map


    Args:
        points: Number of points for the seed and anchor
        iterations: Number of times the map should be updated
    """

    fig, ax = plt.subplots(figsize=(10, 10))
    (line,) = ax.plot([], [], ls="", marker=",", color="black", alpha=0.1)
    ax.set_xlim(-0.1, 4.1)
    ax.set_ylim(-0.05, 1.05)
    ax.set_xlabel("$r$", fontsize=15)
    ax.set_ylabel(r"$x_n$", fontsize=15)
    ax.spines[["right", "top"]].set_visible(False)

    def update(frame):
        r, x = make_logistic_map(points=points, iterations=frame)
        line.set_data(r, x)
        equation = r"$x_{n+1} = rx_{n}(1-x_{n})$, "
        counter = f"for n={frame}"
        line.set_label(equation + counter)
        ax.legend(loc="upper left", frameon=False)
        return (line,)

    ani = animation.FuncAnimation(fig, update, frames=iterations, interval=50)
    ani.save(
        "logistic_map_animation.gif", writer=animation.PillowWriter(fps=15), dpi=200
    )
