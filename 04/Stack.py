def Stack():
    stack = []

    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.append(5)
    print(stack)

    while stack:
        print("pop value is ", stack.pop())


Stack()