from demo import *
import random

def test_order():
    for i in range(10000):
        arr = [random.randint(10, 99) for _ in range(10)]
        
        sort(arr)

        i = 0
        j = len(arr) - 1
        
        while i < j:
            assert(arr[i] <= arr[i + 1])
            i += 1
