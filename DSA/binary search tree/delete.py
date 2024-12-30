class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def find_min(node):
    """Find the node with the minimum key in a subtree."""
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(root, key):
    # If the tree is empty
    if root is None:
        return root  # Key not found

    # Find the node to delete
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        # Node to delete is found
        # Case 1: Node is a leaf
        if root.left is None and root.right is None:
            return None  # Delete the node by returning None
        
        #Case 2: Delete Node with Single Child
        if root.left is None or root.right is None:
            return root.left if not None else root.right
        
        #Case 3: Node with two children
        # Find the inorder successor of the node
        successor = find_min(root.right)
        # Replace the current node's key with the successor's key
        root.key = successor.key
        # Delete the inorder successor
        root.right = delete(root.right, successor.key)

    return root

# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# Test Case 1: Delete a leaf node
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)  # Leaf node
root.left.right = Node(40)
root.right.left = Node(60)
# root.right.right = Node(80)

print("Before Deletion:")
inorder(root)
print()

root = delete(root,50)  # Deleting a leaf node (20)

print("After Deletion:")
inorder(root)
