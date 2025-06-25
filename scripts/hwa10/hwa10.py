from line_profiler import profile
import numpy as np


def isprime(num: int) -> bool:
    if num == 0 or num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


@profile
def run_python() -> np.ndarray:
    pythonarr = np.zeros(shape=len(RANGE), dtype=bool)
    for i, num in enumerate(RANGE):
        boolean = isprime(num)
        pythonarr[i] = boolean
    return pythonarr


if __name__ == "__main__":

    START = 1
    STOP = 10000
    RANGE = range(START, STOP + 1)
    run_python()





