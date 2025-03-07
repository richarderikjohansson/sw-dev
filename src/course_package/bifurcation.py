import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def logistic_equation(x: float, r: float) -> float:
    """Function to calculates the logistic map

    Parameters
    ----------
    x : the seed for the map
    r : the anchor for the map

    Returns
    -------
    xn : map value
    """
    xn = r * x * (1 - x)
    return xn


def make_logistic_map(points: int, iterations: int) -> tuple:
    """Function to return anchors and map value

    Parameters
    ----------
    points : numbers of points that the map should go through for x and r
    iterations : number of iterations that the map should perform for x and r
    """
    r = np.linspace(0, 4, points)
    x = np.random.rand(points)
    for _ in range(iterations):
        x = logistic_equation(x, r)

    return r, x


def plot_map(points: int, iterations: int) -> None:
    """Function to plot the map for a certain number of points and iterations

    Parameters
    ----------
    points : numbers of points that the map should go through for x and r
    iterations : number of iterations that the map should perform for x and r
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
    """Function to animate the map for a certain number of points and iterations

    This function will animate the map from the first iteration to the end of the
    iterations and create an .gif

    Parameters
    ----------
    points : number of points that the map should go through for x and r
    iterations : number of iterations that the map should perform for x and r
    """
    X = []
    R = []
    for iteration in range(iterations):
        r, x = make_logistic_map(points=points, iterations=iteration)
        R.append(r)
        X.append(x)

    fig, ax = plt.subplots(figsize=(10, 10))
    (line,) = ax.plot([], [], ls="", marker=",", color="black", alpha=0.1)
    ax.set_xlim(-0.1, 4.1)
    ax.set_ylim(-0.05, 1.05)
    ax.set_xlabel("$r$", fontsize=15)
    ax.set_ylabel(r"$x_n$", fontsize=15)
    ax.spines[["right", "top"]].set_visible(False)

    def update(frame):
        # skip for n = 0
        if frame > 0:
            line.set_data(R[frame], X[frame])
            equation = r"$x_{n+1} = rx_{n}(1-x_{n})$, "
            counter = f"for n={frame}"
            line.set_label(equation + counter)
            ax.legend(loc="upper left", frameon=False)
        return (line,)

    ani = animation.FuncAnimation(fig, update, frames=iterations, interval=50)
    ani.save(
        "logistic_map_animation.gif", writer=animation.PillowWriter(fps=15), dpi=200
    )
