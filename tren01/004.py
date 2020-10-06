# 0 1 2 3 4 5

import sys

def get(n):
    if n == 0:
        return 0
    else:
        return get(n-1) + n

sys.setrecursionlimit(16000)
n = int(input())
print(get(n))

