# Python program to demonstrate
# insert operation in binary search tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def insert(root, key):
    temp = Node(key)

    # If tree is empty
    if root is None:
        return temp

    # Find the node who is going to 
    # have the new node temp as its child
    parent = None
    curr = root
    while curr is not None:
        parent = curr
        if curr.key > key:
            curr = curr.left
        elif curr.key < key:
            curr = curr.right
        else:
            return root  # Key already exists

    # If key is smaller, make it left 
    # child, else right child
    if parent.key > key:
        parent.left = temp
    else:
        parent.right = temp

    return root

# Recursive Approach
# A utility function to insert
# a new node with the given key
# def insert(root, key):
#     if root is None:
#         return Node(key)
#     if root.val == key:
#             return root
#     if root.val < key:
#             root.right = insert(root.right, key)
#     else:
#             root.left = insert(root.left, key)
#     return root

# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


# Creating the following BST
#      50
#     /  \
#    30   70
#   / \   / \
#  20 40 60 80
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Print inorder traversal of the BST
inorder(r)