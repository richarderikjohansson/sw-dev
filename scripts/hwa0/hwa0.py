import numpy as np


def calc_pi(samples):
    x = np.random.rand(samples) * 2 - 1
    y = np.random.rand(samples) * 2 - 1

    r = np.sqrt(x**2 + y**2)
    pi = 4 * np.sum(r < 1) / samples
    error = np.pi - pi
    print(f"{samples=} give {pi=} with {error=})")


samples = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
for sample in samples:
    calc_pi(sample)
