def max(arr):
    max = arr[0]

    for x in arr:
        while(x > max):
            max = x
    return max

def min(arr):
    min = arr[0]
    for x in arr:
        while(x < min):
            min = x
    return min
