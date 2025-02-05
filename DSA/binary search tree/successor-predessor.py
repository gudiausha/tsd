class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.key = key

root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)