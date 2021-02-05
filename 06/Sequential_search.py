def sequential_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return False


x = [5, 2, 8, 1, 6, 9, 3, 7]
i = sequential_search(x, 3)
print(i)