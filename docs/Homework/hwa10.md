# Making it work: logging and profiling

## Logging

I have actually implemented logging in the software that my current 
Ph.D. project depend on, which can be seen in [KIMRA/ARTS](https://gitlab.irf.se/kimra/ARTS/).
This software, will however be totally rewritten because of everything I learned from in this 
course. This have made me rethink a lot of things, and since this software hopefully will be 
running long after my Ph.D. project is finished I want it to be as good as robust and reliant 
as it can be. 

## Profiling

I actually did this homework assignment after the assignment associated with lecture 12, which 
covered paralellization and foreign function interfaces. Where I tried out Odin lang for the 
first time. What I did in that exercise was to speed up something that I know Python to do 
be slow in, in this case a naive approach to find prime numbers. Down below is the code I 
used in the profiling, and the results from the profiler:

```python
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
```

```
Wrote profile results to hwa10.py.lprof
Timer unit: 1e-06 s

Total time: 0.851963 s
File: hwa10.py
Function: run_python at line 15

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    15                                           @profile
    16                                           def run_python() -> np.ndarray:
    17         1          7.8      7.8      0.0      pythonarr = np.zeros(shape=len(RANGE), dtype=bool)
    18     10001       2126.8      0.2      0.2      for i, num in enumerate(RANGE):
    19     10000     847160.7     84.7     99.4          boolean = isprime(num)
    20     10000       2667.2      0.3      0.3          pythonarr[i] = boolean
    21         1          0.3      0.3      0.0      return pythonarr

```

Again, this was done in a time where I were quite busy with other matters. However, I 
really see how this can be extremely useful to find bottlenecks in the future, and combining
this with things learned when dealing with foreign functions written in for example Odin, I can 
achieve much faster software.
