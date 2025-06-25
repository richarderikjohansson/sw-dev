# Parallelization and foreign function interfaces

## Parallelization

This part I have not done, however, I will definitely have this in mind in the future.
I found it very interesting during the lecture and something that should be implemented 
even for the code I write during my Ph.D. project.

## Foreign functions

This have interested me for a long time, how one should do this. It is such a brute 
force way of speeding up software, but yet elegant in a way. Since I saw Daniels interest
in Odin lang, and having read up on it I also started to get excited about this language I 
choose to use this for the foreign functions. As stated in homework assignment associated 
with Profiling and Logging I implemented a naive way of finding prime numbers in Python. 
This is something that Python is notoriously slow in doing. So I implemented the same thing 
in Odin, and compared how much faster Odin is. I also tried out different compiling settings
for Odin, and they mattered a lot more that anticipated. Below is the Odin function followed
by the Python version:

### Odin
```odin
package isprime

@export
isprime :: proc "c" (num: int) -> bool {

    if num == 0 || num == 1{
        return false
    }

    for i in 2 ..< num {
		if num % i == 0 {
			return false 
		}
	}
	return true 
}

```

### Python
```python
def isprime(num: int) -> bool:
    if num == 0 or num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

```

The compiling settings choosen for Odin were: "default", "speed" and "aggressive". To build
binaries with Odin I had to choose `-build-mode:dll`, on Winshit machines a .dll file is created, But
on UNIX based systems will a .so executable be created. To choose the compiler settings, the optional 
argument `-o:<setting>` be used. Below is the code to load the foreign functions, run these and do some 
comparison with the function implemented in Python:

```Python
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
```

When running this I was not really surprised with the results, but I was very pleased that 
it was so easy to do this in reality. I have always seen this as this super complicated thing
to do. As it turns out it were actually much simpler than I expected. Below is the result for 
the code above

```
--- Python and Odin code to check prime numbers in the range 1-100000 ---


    Execution times for Python and Odin with default compile settings,
    compile settings for speed and aggressive compile settings:

    Python:          26.75099492073059 s
    Odin default:    4.245600938796997 s
    Odin speed:      1.3749580383300781 s
    Odin aggressive: 1.3741164207458496 s

    ---



    Compare how much faster Odin is compared to Python for this calculation:

    Odin default:    6.300873611618939 times faster
    Odin speed:      19.455862779070962 times faster
    Odin aggressive: 19.467779088332673 times faster
```

Seeing that Odin is 19 times faster with a speedy compile setting for this simple problem where only one
function acted as a bottleneck makes me curious when you combine several foreign function interfaces together
where several bottlenecks are present. Very interesting stuff!

