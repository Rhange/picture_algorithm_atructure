def exchange(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def exchange_sort(arr):
    temp = 0
    length = len(arr)
    for _ in range(length - 1):
        i = 0
        for j in range(i + 1, length):
            if arr[i] > arr[j]:
                exchange(arr, i, j)
            i += 1


x = [12, 326, 127, 467, 110, 58]
exchange_sort(x)
print(x)