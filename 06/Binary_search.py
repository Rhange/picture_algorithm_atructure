def binary_search(array, value):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        guess = array[mid]

        if guess == value:
            return [True, mid]
        if guess > value:
            right = mid - 1
        else:
            left = mid + 1
    return [False, 0]


array = range(1, 51)
value = 47

answer = binary_search(array, value)
print(answer)