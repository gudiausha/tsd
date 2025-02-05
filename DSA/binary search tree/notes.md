A **Binary Search Tree (BST)** - https://www2.hawaii.edu/~takebaya/ics211/module8/module8.html
is a specialized binary tree with the following properties that make it efficient for search and traversal operations:

### Key Properties of a BST:
1. **Node Structure**: 
   - Each node has three components:
     - A data value (key).
     - A left child pointer (pointing to the left subtree).
     - A right child pointer (pointing to the right subtree).

2. **Binary Search Property**:
   - For any given node in the BST:
     - The values in the left subtree are **less than** the node’s value.
     - The values in the right subtree are **greater than** the node’s value.
   - This property applies recursively to every node in the tree.

### Operations on a BST:
1. **Search**:
   - Start from the root.
   - If the target value is less than the current node’s value, move to the left child; if greater, move to the right child.
   - Repeat until the value is found or a `null` pointer is reached.
   - Time complexity: **O(h)**, where `h` is the height of the tree. In a balanced BST, \( h = \log_2(n) \).

2. **Insertion**:
   - Follow the binary search property to find the correct position for the new value.
   - Insert the value as a new leaf node.
   - Time complexity: **O(h)**.

3. **Deletion**:
   - Deleting a node can be categorized into three cases:
     1. **Node with no children**: Simply remove the node.
     2. **Node with one child**: Replace the node with its child.
     3. **Node with two children**: Replace the node with its **in-order successor** (smallest value in the right subtree) or **in-order predecessor** (largest value in the left subtree).
   - Time complexity: **O(h)**.

4. **Traversal**:
   - Common traversal techniques:
     1. **In-order Traversal (Left, Root, Right)**:
        - Outputs the nodes in sorted order.
     2. **Pre-order Traversal (Root, Left, Right)**:
        - Useful for creating a copy of the tree.
     3. **Post-order Traversal (Left, Right, Root)**:
        - Useful for deleting or freeing nodes in memory.

### Advantages of BST:
- Efficient for operations like search, insert, and delete when the tree is balanced.
- Provides sorted data via in-order traversal.

### Drawbacks:
- If the tree becomes **unbalanced** (e.g., a linked list due to sequential insertions), the time complexity degrades to **O(n)**.
- To avoid this, use **self-balancing BSTs** like AVL trees or Red-Black trees.

---

### **Unbalanced BST:**
An **unbalanced Binary Search Tree (BST)** is a BST where the height difference between the left and right subtrees of one or more nodes becomes significantly large. This typically happens when the nodes are inserted in a way that creates a skewed structure, resembling a linked list. 

#### Characteristics of an Unbalanced BST:
1. **Skewed Structure**: 
   - In the worst case, all nodes are on one side (e.g., inserting sorted data into an empty BST).
   - Example:  
     ```
     Insert 1 → 2 → 3 → 4 → 5 → 6
         1
          \
           2
            \
             3
              \
               4
                \
                 5
     ```
2. **Degraded Performance**:
   - Operations like search, insert, and delete no longer take \( O(\log_2(n)) \); they degrade to **O(n)** because traversal must visit every node.
3. **Imbalance Causes**:
   - Sequential or sorted insertions without restructuring.
   - No mechanism to ensure balance during insertions or deletions.

---

### **Self-Balancing BST:**
A **self-balancing Binary Search Tree** is a type of BST that maintains a balance between its left and right subtrees automatically, ensuring the tree remains approximately balanced after every insertion or deletion. 

#### Characteristics of a Self-Balancing BST:
1. **Balance Condition**:
   - The height of the left and right subtrees of any node differs by no more than a fixed threshold (usually 1).
   - This keeps the height \( h \) proportional to \( \log_2(n) \), ensuring efficient operations.

2. **Balanced Structure**:
   - Example: Inserting the same sequence (1 → 2 → 3 → 4 → 5) into a self-balancing BST results in:
     ```
         3
       /   \
      2     5
     /     /
    1     4
     ```

3. **Performance**:
   - Maintains \( O(\log_2(n)) \) time complexity for search, insert, and delete.

---

### Types of Self-Balancing BSTs:
1. **AVL Tree**:
   - Named after its inventors (Adelson-Velsky and Landis).
   - Maintains a **balance factor**: the difference in height between the left and right subtrees of any node.
   - Balance factor must be between -1 and 1.
   - If the tree becomes unbalanced after an operation, it performs **rotations** to restore balance.

2. **Red-Black Tree**:
   - Maintains balance using **color properties** (each node is either red or black).
   - Ensures that the longest path from the root to a leaf is no more than twice the shortest path.
   - Used in many libraries like C++ STL `map` and `set`.

3. **B-Tree**:
   - Used in database indexing.
   - Generalized BST where nodes can have multiple children.
   - Ensures balance by redistributing keys and splitting nodes as needed.

4. **Splay Tree**:
   - A self-adjusting BST that brings the most recently accessed node to the root, optimizing for frequently accessed elements.

---

### Example: AVL Tree Balancing
#### Rotations:
1. **Left Rotation**: Used to balance a right-heavy tree.
2. **Right Rotation**: Used to balance a left-heavy tree.
3. **Left-Right Rotation**: A combination of left and right rotation.
4. **Right-Left Rotation**: A combination of right and left rotation.

#### Visual Example of AVL Tree Rotation:
**Before Insertion of 50**:
```
      30
     /  \
   20    40
             \
              50
```
**After Rotation (Balancing)**:
```
       40
      /  \
    30    50
   /
  20
```

---

### When to Use Self-Balancing BSTs:
- When the data is dynamic and insertions/deletions happen frequently.
- When maintaining \( O(\log_2(n)) \) time complexity is critical for performance (e.g., databases, caching systems).
---

### **Explanation of the Important Points about BST**

#### 1. **Utility of a Binary Search Tree (BST):**
   - A BST maintains a sorted stream of data due to its structure, where the left child contains values smaller than the parent, and the right child contains values greater.
   - This structure allows efficient operations like:
     - **Search**: Locating a specific value.
     - **Insert**: Adding a new value at its correct position while maintaining the BST property.
     - **Delete**: Removing a value and restructuring the tree if necessary.
     - **Ceiling**: Finding the smallest value greater than or equal to a given key.
     - **Maximum and Minimum**: Finding the largest and smallest values in the BST.

   All these operations take \( O(h) \), where \( h \) is the height of the tree.

---

#### 2. **Traversal in Sorted Order:**
   - Using an **in-order traversal** (left, root, right), the items in a BST can be listed in ascending order efficiently.

---

#### 3. **Self-Balancing BSTs and \( O(\log n) \) Operations:**
   - A **Self-Balancing BST** (like AVL or Red-Black Tree) ensures that the height \( h \) is always proportional to \( \log_2(n) \), where \( n \) is the number of nodes.
   - This is achieved through mechanisms like rotations or color rules that prevent the tree from becoming skewed (unbalanced).
   - As a result:
     - Operations like search, insert, and delete always take \( O(\log n) \) time in a self-balancing BST.

---

#### 4. **Hash Table vs. BST:**
   - **Hash Table**:
     - Supports **search, insert, and delete** in \( O(1) \) time on average, using hashing.
     - However, hash tables do not maintain order, and operations like ceiling, maximum, and minimum are not straightforward.
   - **BST**:
     - Maintains a sorted order of elements and supports operations like traversal in sorted order, ceiling, and floor efficiently.
     - These operations are difficult or inefficient to perform in a hash table.

   Use hash tables when **order is not important**, and only search, insert, and delete are needed. Use BSTs when **order and additional operations** are required.

---

### **Height and Length of a Tree**

#### 1. **Height of a Tree:**
   - **Definition**: 
     - The height of a tree is the number of edges on the longest path from the root to a leaf.
     - A tree with a single node (root) has a height of 0.
   - **Calculation**:
     - Recursively compute the height of the left and right subtrees, then take the maximum of the two and add 1.
   - **Formula**:
     \[
     \text{Height of a node} = 1 + \max(\text{Height of left subtree}, \text{Height of right subtree})
     \]
   - **Example**:
     ```
           10
          /  \
         5    15
        / \
       3   7
     ```
     - Height of the tree = \( 1 + \max(Height(5), Height(15)) \).
     - Height of node 5 = \( 1 + \max(Height(3), Height(7)) = 1 + 1 = 2 \).

#### 2. **Length of a Tree (or Total Number of Nodes):**
   - **Definition**: 
     - The length of a tree refers to the total number of nodes in the tree.
   - **Calculation**:
     - Recursively compute the number of nodes in the left and right subtrees, then add 1 for the root.
   - **Formula**:
     \[
     \text{Length of the tree} = 1 + (\text{Length of left subtree} + \text{Length of right subtree})
     \]
   - **Example**:
     ```
           10
          /  \
         5    15
        / \
       3   7
     ```
     - Length of the tree = \( 1 + (Length(5) + Length(15)) \).
     - Length of subtree rooted at 5 = \( 1 + (Length(3) + Length(7)) = 3 \).
     - Total length = \( 1 + 3 + 1 = 5 \).

---

### Summary Table:
| Operation        | BST (\(O(h)\)) | Self-Balancing BST (\(O(\log n)\)) | Hash Table (\(O(1)\)) |
|-------------------|----------------|------------------------------------|-----------------------|
| **Search**        | \(O(h)\)       | \(O(\log n)\)                     | \(O(1)\) (average)    |
| **Insert**        | \(O(h)\)       | \(O(\log n)\)                     | \(O(1)\) (average)    |
| **Delete**        | \(O(h)\)       | \(O(\log n)\)                     | \(O(1)\) (average)    |
| **Sorted Order**  | \(O(n)\)       | \(O(n)\)                          | Not supported         |
| **Ceiling/Floor** | \(O(h)\)       | \(O(\log n)\)                     | Not supported         |

---

A **Binary Search Tree (BST)** can be traversed using **all three types of tree traversal techniques** (in-order, pre-order, and post-order). Each traversal serves a different purpose and outputs the nodes in a specific order.

---

### **1. In-Order Traversal** (Left → Root → Right)
- **Description**: Traverses the left subtree first, then visits the root node, and finally traverses the right subtree.
- **Output**: For a BST, **in-order traversal always results in a sorted sequence** of the tree's elements.
- **Use Case**:
  - To retrieve elements in sorted order.
  - Commonly used when the goal is to iterate over the BST like a sorted list.

**Example**:
For this BST:
```
      10
     /  \
    5    15
   / \
  2   7
```
In-order traversal: **2, 5, 7, 10, 15**

---

### **2. Pre-Order Traversal** (Root → Left → Right)
- **Description**: Visits the root node first, then traverses the left subtree, followed by the right subtree.
- **Output**: The order in which nodes are visited during pre-order traversal highlights the tree's hierarchical structure.
- **Use Case**:
  - To create a **copy of the tree** (by traversing nodes in the same hierarchical order as they appear).
  - Used in applications where the **root node** must be processed before its children.

**Example**:
For the same BST:
Pre-order traversal: **10, 5, 2, 7, 15**

---

### **3. Post-Order Traversal** (Left → Right → Root)
- **Description**: Traverses the left subtree first, then the right subtree, and finally visits the root node.
- **Output**: The order in which nodes are visited emphasizes the children being visited before their parent.
- **Use Case**:
  - Used in **deleting or freeing nodes** in a tree.
  - Helps in **evaluating expressions** represented as binary trees.

**Example**:
For the same BST:
Post-order traversal: **2, 7, 5, 15, 10**

---

### Choosing the Right Traversal in a BST:
| **Traversal**  | **When to Use**                                                                                   | **Output Order in BST**           |
|-----------------|--------------------------------------------------------------------------------------------------|------------------------------------|
| **In-Order**   | When you need elements in sorted order.                                                           | Sorted ascending order.           |
| **Pre-Order**  | When you want to process the root first (e.g., creating/copying a tree).                          | Root node appears first.          |
| **Post-Order** | When you want to process children before the root (e.g., deleting all nodes, evaluating subtrees). | Root node appears last.           |

---

### Additional Notes:
- **In-order traversal** is unique to BST in that it naturally produces a sorted sequence, which isn't necessarily true for other binary trees.
- A BST's structure enables any of these traversals to operate efficiently, but the **specific use case** determines which traversal to use. 

---
The **time complexity** (TC) and **space complexity** (SC) of the **search operation in a Binary Search Tree (BST)** can be analyzed for both the **recursive** and **iterative** approaches.

### **Time Complexity (TC) of Search in BST**

1. **Recursive Approach:**
   - The **time complexity** of the search operation depends on the **height of the tree** (`h`).
   - In the worst case, you may need to traverse from the root to a leaf node, visiting every level of the tree.
   
   - **Best case**: The root node contains the key you're looking for, so the time complexity is **O(1)**.
   - **Worst case**: The tree is unbalanced (e.g., a linked list), and you must traverse all the way to a leaf node. This means the time complexity is **O(h)**, where `h` is the height of the tree.
   - **Average case**: If the tree is balanced, the height `h` is logarithmic with respect to the number of nodes, i.e., `h = log(n)`, where `n` is the number of nodes. In this case, the time complexity is **O(log n)**.

   - **Overall**: The time complexity of the recursive search operation is:
     - **Worst case**: **O(h)**, where `h` is the height of the tree.
     - **Average case**: **O(log n)** (for balanced trees).
     - **Best case**: **O(1)**.

2. **Iterative Approach:**
   - The **time complexity** for the iterative approach is the same as for the recursive approach because both methods perform the same number of operations in the worst case. 
   - Like the recursive approach, the iterative approach will traverse the tree from the root to the target key, visiting each level.
   
   - **Best case**: **O(1)** (if the key is at the root).
   - **Worst case**: **O(h)** (if the tree is unbalanced and you traverse down to a leaf node).
   - **Average case**: **O(log n)** (for balanced trees).

   - **Overall**: The time complexity of the iterative search operation is:
     - **Worst case**: **O(h)**.
     - **Average case**: **O(log n)**.
     - **Best case**: **O(1)**.

---

### **Space Complexity (SC) of Search in BST**

1. **Recursive Approach:**
   - In the recursive approach, each recursive call uses **stack space** to keep track of the function calls.
   - The depth of the recursion depends on the height of the tree (`h`).
   - In the worst case (unbalanced tree), the recursion depth is equal to the height of the tree, which is **O(h)**.
   - In the best case (balanced tree), the recursion depth is logarithmic, i.e., **O(log n)**.

   - **Overall**:
     - **Worst case**: **O(h)** (height of the tree).
     - **Best case**: **O(log n)** (for balanced trees).

2. **Iterative Approach:**
   - In the iterative approach, no recursion occurs, so there is no additional stack space required for function calls.
   - The iterative approach typically uses a constant amount of extra space, i.e., **O(1)**, except for the space used by the input tree (which is **O(n)** for storing the nodes).
   
   - **Overall**: The space complexity is:
     - **O(1)** (constant space) for the iterative approach.

---

### **Summary**

| Approach         | Time Complexity (Worst) | Time Complexity (Average) | Time Complexity (Best) | Space Complexity |
|------------------|-------------------------|---------------------------|------------------------|------------------|
| **Recursive**     | O(h)                    | O(log n)                  | O(1)                   | O(h)             |
| **Iterative**     | O(h)                    | O(log n)                  | O(1)                   | O(1)             |

- **Recursive** approach requires **O(h)** space for function call stack.
- **Iterative** approach requires **O(1)** space, using only constant space for the traversal.

For **balanced** BSTs, both the time complexity and space complexity are **O(log n)**, while for **unbalanced** BSTs, the complexity can degrade to **O(n)**, where `n` is the number of nodes in the tree.

---
### Leaf Node Deletion Case
The key to understanding why we only return `None` and don't explicitly assign the parent node's `left` or `right` to `None` lies in how the recursive function works.

---

### **How Recursion Updates the Parent Node's Pointer**
When we write:

```python
root.left = delete(root.left, key)
root.right = delete(root.right, key)
```

We are explicitly assigning the **returned value of the recursive call** to `root.left` or `root.right`. This ensures that the parent's reference (either `left` or `right`) is updated based on the result of the `delete` function.

Let’s break it down step by step for the **else** case (when the node is a leaf):

1. **Node Found**:  
   Suppose we find the node with the matching key, and it is a leaf node (i.e., `root.left is None` and `root.right is None`).

2. **Return `None`**:  
   By returning `None` in the `delete` function, we are effectively signaling that the node should be removed from the tree.

3. **Parent Updates Its Pointer**:  
   - If the parent called `delete(root.left, key)`, then the `delete` function returns `None` for `root.left`, and the parent updates its `left` pointer to `None`.
   - Similarly, if the parent called `delete(root.right, key)`, the parent's `right` pointer gets updated to `None`.

---

### **Why Don’t We Directly Update the Parent’s Pointer?**
We don’t directly update the parent’s `left` or `right` in the `else` block because:
1. **Parent Reference is Not Explicitly Passed**:  
   The `delete` function operates on the current node (`root`). It doesn’t have direct access to the parent node's `left` or `right` pointers.
   
2. **The Recursive Call Handles Updates**:  
   By returning `None`, we allow the recursive call to automatically handle the update of the parent’s pointer, as shown in:

   ```python
   root.left = delete(root.left, key)
   root.right = delete(root.right, key)
   ```

---

### **An Analogy**
Think of the recursive function as a helper that you hire to clean up branches of a tree. Instead of the helper going back to report what they’ve cleaned, they simply return the modified branch. The tree owner (the parent node) then attaches the returned branch to the correct position.

---

### **Illustrative Example**
Let’s assume the tree is:

```
      50
     /  \
    30   70
   /
  20
```

Now, we want to delete the leaf node `20`.

1. **Initial Call**:  
   `delete(root, 20)` is called with `root` pointing to `50`.

2. **Traverse Left**:  
   Since `20 < 50`, it calls `delete(root.left, 20)` where `root.left` is `30`.

3. **Traverse Left Again**:  
   Since `20 < 30`, it calls `delete(root.left, 20)` where `root.left` is `20`.

4. **Match Found**:  
   `20 == root.key`, and `root.left` and `root.right` are `None`. The function returns `None` (deleting the leaf).

5. **Update Parent’s Pointer**:  
   Back at the node `30`, the statement `root.left = delete(root.left, 20)` assigns `None` to `30.left`.

6. **Propagate Up**:  
   This updated tree structure propagates up to `50`, ensuring the tree remains valid.

After deletion, the tree becomes:

```
      50
     /  \
    30   70
```

---

### **Key Takeaway**
We don’t need to explicitly update the parent’s `left` or `right` pointer in the `else` block because the recursive call handles it automatically. The parent node's pointer is updated when the recursive call returns the modified subtree (or `None` if the node was deleted).

---

In a **Binary Search Tree (BST)**, the **inorder predecessor** and **inorder successor** of a node are defined relative to the sorted order of the tree.

### **Inorder Predecessor**
The **inorder predecessor** of a node is the node that comes immediately **before** it in an inorder traversal (sorted order).

#### **Cases to Find Inorder Predecessor**
1. **If the left subtree exists:**
   - The inorder predecessor is the **rightmost node** in the left subtree.
2. **If the left subtree does not exist:**
   - Traverse up the tree using the parent pointer until you find a node that is a **right child** of its parent. That parent will be the inorder predecessor.

---

### **Inorder Successor**
The **inorder successor** of a node is the node that comes immediately **after** it in an inorder traversal (sorted order).

#### **Cases to Find Inorder Successor**
1. **If the right subtree exists:**
   - The inorder successor is the **leftmost node** in the right subtree.
2. **If the right subtree does not exist:**
   - Traverse up the tree using the parent pointer until you find a node that is a **left child** of its parent. That parent will be the inorder successor.

---

### **Examples**

Consider this BST:
```
        20
       /  \
     10    30
    /  \      \
   5   15      40
```

1. **Inorder Traversal**: `5, 10, 15, 20, 30, 40`
   
   - Inorder predecessor of `20` is `15`.
   - Inorder successor of `20` is `30`.

2. **For `10`:**
   - Inorder predecessor: `5`.
   - Inorder successor: `15`.

### **Time Complexity**
- **Finding Predecessor/Successor in a BST**:
  - **Best case**: \(O(1)\) (direct child).
  - **Worst case**: \(O(h)\), where \(h\) is the height of the tree.
- **Space Complexity**: \(O(1)\) for iterative methods.

---