class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def init():
    global node1    # global
    node1 = Node(1) # Node instance 생성 및 data 입력
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2  # next 입력
    node2.next = node3
    node3.next = node4  # node4는 입력안했으므로 default 값인 None이 들어가 있다.


def delete(del_data):   # 구성된 리스트에서 데이터를 지우고, 나머지를 연결한다.
    global node1
    pre_node = node1
    next_node = pre_node.next

    if pre_node.data == del_data:
        node1 = next_node
        del pre_node
        return
    
    while next_node:
        if next_node.data == del_data:
            pre_node.next = next_node.next
            del next_node
            break
        pre_node = next_node
        next_node = next_node.next


def insert(ins_data):   # insert data to linked list
    global node1
    new_node = Node(ins_data)
    new_node.next = node1
    node1 = new_node


def print_list():   # print data for linked list
    global node1
    node = node1
    while node:
        print(node.data)
        node = node.next
    print()


def LinkedList():
    init()  # 4개의 노드 생성 및 연결
    delete(2)   # 데이터 값이 2 인 노드 삭제
    insert(9)   # 데이터 값이 9인 새로운 노드 추가
    print_list()    # 출력


LinkedList()