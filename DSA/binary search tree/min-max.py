class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.key = key

def minValue(root):
    # base case
    if root is None:
        return -1
    curr = root
    while curr.left is not None:
        curr = curr.left
    
    print(curr.key)

def maxValue(root):
    # base case
    if root is None:
        return -1
    curr = root
    while curr.right is not None:
        curr = curr.right
    
    print(curr.key)

root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)

print('The min value in BST is', end=" ")
minValue(root)
print()

print('The max value in BST is', end = " ")
maxValue(root)

