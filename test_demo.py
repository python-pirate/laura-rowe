import random
from demo import *

def test_max():
    for i in range(100):
        arr = []
        for j in range(10):
            arr.append(random.randint(10, 99))

        m = max(arr)

        for x in arr:
            assert(m >= x)

def test_min():
    for i in range(100):
        arr = []
        for j in range(10):
            arr.append(random.randint(10, 99))

        n = min(arr)

        for x in arr:
            assert(n <= x)

##################################
