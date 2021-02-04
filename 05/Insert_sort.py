def insert_sort(arr):
    for size in range(1, len(arr)):
        val = arr[size]
        i = size

        while i > 0 and arr[i - 1] > val:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = val


x = [5, 2, 8, 6, 1, 9, 3, 7]
insert_sort(x)
print(x)
