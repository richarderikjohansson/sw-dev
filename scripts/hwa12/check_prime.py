import ctypes
import time
from ctypes import c_int, c_bool
import numpy as np
from pathlib import Path

START = 1
STOP = 100000
RANGE = range(START, STOP + 1)

odinlib_default_compile = Path.cwd() / "isprime_default.so"
odinlib_speed_compile = Path.cwd() / "isprime_speed.so"
odinlib_aggressive_compile = Path.cwd() / "isprime_aggressive.so"

lib_default = ctypes.CDLL(str(odinlib_default_compile))
lib_default.isprime.restype = c_bool
lib_default.isprime.argtypes = [c_int]

lib_speed = ctypes.CDLL(str(odinlib_speed_compile))
lib_speed.isprime.restype = c_bool
lib_speed.isprime.argtypes = [c_int]

lib_aggressive = ctypes.CDLL(str(odinlib_aggressive_compile))
lib_aggressive.isprime.restype = c_bool
lib_aggressive.isprime.argtypes = [c_int]


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        exectime = end - start
        return result, exectime

    return wrapper


def isprime(num: int) -> bool:
    if num == 0 or num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def print_results(start, end, *exectimes) -> None:
    execpy = exectimes[0]
    execodin_default = exectimes[1]
    execodin_speed = exectimes[2]
    execodin_aggressive = exectimes[3]

    exectimes_str = f"""

    Execution times for Python and Odin with default compile settings,
    compile settings for speed and aggressive compile settings:

    Python:          {execpy} s
    Odin default:    {execodin_default} s
    Odin speed:      {execodin_speed} s
    Odin aggressive: {execodin_aggressive} s

    ---

    """

    execcompare_str = f"""
    Compare how much faster Odin is compared to Python for this calculation:

    Odin default:    {execpy / execodin_default} times faster
    Odin speed:      {execpy / execodin_speed} times faster
    Odin aggressive: {execpy / execodin_aggressive} times faster

    """
    print(
        f"--- Python and Odin code to check prime numbers in the range {start}-{end} ---"
    )
    print(exectimes_str)
    print(execcompare_str)


@timer
def odin_default() -> np.ndarray:
    odinarr = np.zeros(shape=len(RANGE), dtype=bool)
    for i, num in enumerate(RANGE):
        boolean = lib_default.isprime(num)
        odinarr[i] = boolean
    return odinarr


@timer
def odin_speed() -> np.ndarray:
    odinarr = np.zeros(shape=len(RANGE), dtype=bool)
    for i, num in enumerate(RANGE):
        boolean = lib_speed.isprime(num)
        odinarr[i] = boolean
    return odinarr


@timer
def odin_aggressive() -> np.ndarray:
    odinarr = np.zeros(shape=len(RANGE), dtype=bool)
    for i, num in enumerate(RANGE):
        boolean = lib_aggressive.isprime(num)
        odinarr[i] = boolean
    return odinarr


@timer
def run_python() -> np.ndarray:
    pythonarr = np.zeros(shape=len(RANGE), dtype=bool)
    for i, num in enumerate(RANGE):
        boolean = isprime(num)
        pythonarr[i] = boolean
    return pythonarr


pythonarr, pythonexec = run_python()
odinarr_default, odinexec_default = odin_default()
odinarr_speed, odinexec_speed = odin_speed()
odinarr_aggressive, odinexec_aggressive = odin_aggressive()

all_equal = (
    np.array_equal(pythonarr, odinarr_default)
    and np.array_equal(odinarr_default, odinarr_speed)
    and np.array_equal(odinarr_speed, odinarr_aggressive)
)

assert all_equal
print_results(
    START,
    STOP,
    pythonexec,
    odinexec_default,
    odinexec_speed,
    odinexec_aggressive,
)
