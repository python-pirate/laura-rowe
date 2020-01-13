import random
from demo import *

def test_max():
    arr = []
    for i in range(10):
        arr.append(random.randint(10, 99))

    m = max(arr)

    for x in arr:
        assert(m >= x)

def test_min():
    arr = []
    for i in range(10):
        arr.append(random.randint(10, 99))

    n = min(arr)

    for x in arr:
        assert(n <= x)
