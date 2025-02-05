class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.key = key

def inorder_traversal(root):
    if root is None:
        return
    
    inorder_traversal(root.left)
    print(root.key,end=" ")
    inorder_traversal(root.right)

def inorder_traversal_desc(root):
    if root is None:
        return
    
    inorder_traversal_desc(root.right)
    print(root.key,end=" ")
    inorder_traversal_desc(root.left)

def preorder_traversal(root):
    if root is None:
        return
    
    print(root.key,end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def postorder_traversal(root):
    if root is None:
        return
    
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.key,end=" ")

root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)

print("Inorder Traversal",end=" ")
inorder_traversal(root)
print()

print("Inorder Traversal Desc",end=" ")
inorder_traversal_desc(root)
print()

print('Preorder Traversal',end=" ")
preorder_traversal(root)
print()

print("Postorder Traversal",end=" ")
postorder_traversal(root)

'''
Step-by-Step Execution of Inorder Traversal

Start at the root (5).
Traverse the left subtree of 5 → Go to 3.
Traverse the left subtree of 3 → Go to 2.
2 has no left child → Print 2.
Go back to 3 → Print 3.
Traverse the right subtree of 3 → Go to 4.
4 has no left child → Print 4.
Go back to 5 → Print 5.
Traverse the right subtree of 5 → Go to 7.
Traverse the left subtree of 7 → Go to 6.
6 has no left child → Print 6.
Go back to 7 → Print 7.
Traverse the right subtree of 7 → Go to 8.
8 has no left child → Print 8.
'''