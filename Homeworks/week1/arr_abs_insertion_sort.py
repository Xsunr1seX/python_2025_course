def insertionSort(arr):
    for i in range(1, len(arr)):
        sort = i - 1
        while sort > -1 and (arr[sort] > arr[sort+1]):
            arr[sort],arr[sort+1] = arr[sort+1], arr[sort]
            sort -= 1
    return arr

# input
a = [-3, -2, 0, 1, 3, 5]
#     |               |
a = [abs(i) for i in a]
print(a)
# result [0, 1, 2, 3, 3, 5]
g = insertionSort(a)
print(g)
