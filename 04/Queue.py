def Queue():

    queue = []
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    queue.append(5)
    print(queue)

    while queue:
        print(f"Get Value : {queue.pop(0)}")  # pop() 안에 index 0를 넣어주면 맨 앞에꺼를 빼낸다.


Queue()