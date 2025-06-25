from numpy import loadtxt
import numpy as np


def approach1():
    arrs = loadtxt("lists.txt", dtype=int)
    s = np.sum(np.abs(np.sort(arrs[:, 0]) - np.sort(arrs[:, 1])))
    print(s)


def approach2():
    arrs = loadtxt("lists.txt", dtype=int)
    s = 0
    for i, j in zip(arrs[:, 0], arrs[:, 1]):
        s += abs(i - j)
    print(s)


def approach3():
    l1 = []
    l2 = []
    with open("lists.txt", "r") as fh:
        content = fh.readlines()

    for line in content[0:-1]:
        l1.append(int(line.split()[0]))
        l2.append(int(line.split()[1]))

    s = 0
    for n, m in zip(sorted(l1), sorted(l2)):
        s += abs(n - m)
    print(s)


approach3()
