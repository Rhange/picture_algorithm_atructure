class Node(object):  # Node의 형식을 정의하는 부분
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinarySearchTree(object):  # 이진 트리에 데이터를 넣는 부분
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:  # base case
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)  # recursive case
            else:
                node.right = self._insert_value(node.right, data)  # recursive case
        return node

    def find(self, key):  # 이진 트리에서 데이터를 찾는 부분
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:  # base case
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)  # recursive case
        else:
            return self._find_value(root.right, key)  # recursive case

    def delete(self, key):  # 이진 트리에서 데이터를 지우는 부분
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:  # base case
            return node, False

        deleted = False
        if key == node.data:  # base case?
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.left
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)  # recursive
        else:
            node.right, deleted = self._delete_value(node.right, key)  # recursive
        return node, deleted

    def DFTravel(self):  # 데이터를 출력하는 부분, 깊이 우선 탐색: 루트 > 왼쪽 노드 > 오른쪽 노드
        def _DFTravel(root):
            if root is None:  # base case
                pass
            else:
                print(root.data, end=" ")
                _DFTravel(root.left)  # recursive case, call stack first
                _DFTravel(root.right)  # recursive case, call stack second

        _DFTravel(self.root)

    def LFTravel(self):  # 데이터를 출력하는 부분, 깊이 우선 탐색: 왼쪽 노드 > 루트 > 오른쪽 노드
        def _LFTravel(root):
            if root is None:  # base case
                pass
            else:
                _LFTravel(root.left)
                print(root.data, end=" ")
                _LFTravel(root.right)

        _LFTravel(self.root)

    def LRTravel(self):  # 데이터를 출력하는 부분, 깊이 우선 탐색: 왼쪽 노드 > 오른쪽 노드 > 루트
        def _LRTravel(root):
            if root is None:
                pass
            else:
                _LRTravel(root.left)
                _LRTravel(root.right)
                print(root.data, end=" ")

        _LRTravel(self.root)

    def layerTravel(self):  # 데이터를 출력하는 부분, 너비 우선 탐색:
        def _layerTravel(root):

            queue = [root]
            while queue:  # queue가 빈 리스트면 스탑
                root = queue.pop(0)  # 앞에서부터 하나씩 꺼내서 루트로 지정
                if root is not None:  # base case
                    print(root.data, end=" ")
                    if root.left:
                        queue.append(root.left)  # 왼쪽 노드가 있으면 recursive, queue에 왼쪽부터 append 한다.
                    if root.right:
                        queue.append(root.right)  # 오른쪽 노드가 있으면 recursive,

        _layerTravel(self.root)


# 데이터 선언
data = [20, 6, 8, 12, 78, 32, 65, 32, 7, 9]
tree = BinarySearchTree()

# 트리 구조 완성하기
for x in data:
    tree.insert(x)

# 트리 안의 데이터 존재에 대한 확인 및 조작
print(tree.find(9))
print(tree.find(3))
print(tree.delete(78))
print(tree.delete(6))
print(tree.delete(11))

# 트리 구조의 데이터 출력
print("\n@@@@@@")
tree.DFTravel()  # 깊이 우선 탐색 중 전위 순회: 뿌리 > 왼쪽 트리 > 오른쪽 트리
print("\n=======")
tree.LFTravel()  # 깊이 우선 탐색 중 중위 순회: 왼쪽 트리 > 뿌리 > 오른쪽 트리
print("\n*******")
tree.LRTravel()  # 깊이 우선 탐색 중 후위 순회: 왼쪽 트리 > 오른쪽 트리 > 뿌리 노드
print("\n&&&&&&&")
tree.layerTravel()  # 너비 우선 탐색 : 뿌리 노드부터 깊이순으로 방문