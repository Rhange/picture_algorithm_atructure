def Between(arr, start, ranges):
    for target in range(start + ranges, len(arr)):
        val = arr[target]
        i = target
        while i > start:
            if arr[i - ranges] > val:
                arr[i] = arr[i - ranges]
            else:
                break
            i -= ranges
        arr[i] = val


def shell_sort(arr):
    ranges = len(arr) // 2
    while ranges > 0:
        for start in range(ranges):
            Between(arr, start, ranges)
        ranges = ranges // 2


arr = [5, 2, 8, 6, 1, 9, 3, 7]
shell_sort(arr)
print(arr)