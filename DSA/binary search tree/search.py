class TreeNode():
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

#recursive way
def search(root, key):
    if root is None:
        return "The key is not available"  # Base case: Tree/subtree is empty.
    elif root.key == key:
        return "The Key is available"  # Base case: Key matches the node value.
    elif root.key < key:
        return search(root.right, key)  # Recur on the right subtree.
    else:
        return search(root.left, key)  # Recur on the left subtree.

#iterative approach
def search(root,key):
    curr = root
    while curr is not None:
        if curr.key == key:
            return "The Key is available"
        elif curr.key < key:
            curr = curr.right
        else:
            curr = curr.left
    else:
        return "The key is not available"

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

# print(vars(root.left))
# print(dir(root))

output = search(root,6)
print(output)