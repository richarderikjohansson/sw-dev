import numpy as np
import matplotlib.pyplot as plt


def sigmoid(start: int | float, stop: int | float, num: int):
    """Function to calculate a Sigmoid function

    Parameters
    ----------
    start: lower bound for the function
    stop: upper bound for the function
    num: the amount of point between start and stop

    Returns
    -------
    t (np.array): array that the sigmoid function have been
      calculated on
    sigmoid (np.array): array of values from the sigmoid function


    """
    t = np.linspace(start=start, stop=stop, num=num)
    sigmoid = 1 / (1 + np.exp(-t))

    return t, sigmoid


# figure 1
t, sig = sigmoid(start=-10, stop=10, num=50)
y_values = [0, 0.5, 1.0]
linestyles = ["--", ":", "--"]

fig, ax = plt.subplots()
for y, linestyle in zip(y_values, linestyles):
    ax.axhline(y=y, color="black", linestyle=linestyle)

ax.axline((0, 0.5), slope=0.25, color="black", linestyle=(0, (5, 5)))
ax.plot(t, sig, linewidth=2, label=r"$\sigma(t) = \frac{1}{1 + e^{-t}}$")
ax.set(xlim=(-10, 10), xlabel="t")
ax.legend(fontsize=14)

# figure 2
fig, ax = plt.subplots()
for pos in np.linspace(-2, 1, 10):
    ax.axline((pos, 0), slope=0.5, color="k", transform=ax.transAxes)

ax.set(xlim=(0, 1), ylim=(0, 1))
plt.show()
