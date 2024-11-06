# RECURSION

import sys

sys.setrecursionlimit(2000)
n = 1

def python():
    global n
    n += 1
    print("PYTHON ", n)
    python()

python()