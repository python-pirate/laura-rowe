import random
from demo import *

def test_max_min():
    arr = []
    for i in range(10):
        arr.append(random.randint(10, 99))
    max = max_min()
    for x in arr:
        assert(max >= x)
        