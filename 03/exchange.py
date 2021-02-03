def exchange(a, b):
    temp = a
    a = b
    b = temp
    return a, b

a = 10
b = 20

a, b = exchange(a, b)

print(a, b)

a, b = b, a

print(a, b)