# DSA 08: Binary Trees

A **binary tree** is a tree where every node has **at most two children**, conventionally called `left` and `right`. This constraint (max 2 children) is what makes binary trees so useful and analyzable — most tree algorithms you'll meet in interviews and real systems are binary trees or their descendants (BSTs, heaps, AVL trees).

---

## 1. The Node

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

```
        1
       / \
      2   3
     / \
    4   5
```

```python
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
```

---

## 2. Types of Binary Trees

| Type | Definition |
|---|---|
| **Full** | Every node has 0 or 2 children (never exactly 1) |
| **Complete** | Every level is fully filled except possibly the last, which fills left-to-right |
| **Perfect** | Every internal node has 2 children AND every leaf is at the same depth |
| **Balanced** | Height stays O(log n) — the difference in height between left/right subtrees is bounded (this is what AVL trees enforce automatically) |
| **Degenerate/Pathological** | Every node has only one child — effectively a linked list, worst case O(n) height |

---

## 3. The Three Depth-First Traversals

These differ only in *when* you visit the current node relative to its children:

```python
def inorder(node):     # Left, Node, Right — gives sorted order for a BST
    if node is None:
        return
    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)

def preorder(node):    # Node, Left, Right — useful for copying/serializing a tree
    if node is None:
        return
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)

def postorder(node):   # Left, Right, Node — useful for safely deleting a tree bottom-up
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=" ")
```

For the tree above:
- inorder:   `4 2 5 1 3`
- preorder:  `1 2 4 5 3`
- postorder: `4 5 2 3 1`

---

## 4. Level-Order Traversal (Breadth-First)

```python
from collections import deque

def level_order(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

---

## 5. Height and Size

```python
def height(node):
    if node is None:
        return -1               # convention: empty tree has height -1, single node has height 0
    return 1 + max(height(node.left), height(node.right))

def size(node):
    if node is None:
        return 0
    return 1 + size(node.left) + size(node.right)
```

---

## 📚 Resources

- **W3Schools:** [DSA Binary Trees](https://www.w3schools.com/dsa/dsa_data_binarytrees.php) · [Binary Tree Traversal](https://www.w3schools.com/dsa/dsa_data_binarytrees_traversal.php)
- **YouTube:** [mycodeschool — Binary Tree Traversal (Inorder/Preorder/Postorder)](https://www.youtube.com/watch?v=gm8DUJJhmY4)
- **YouTube:** [William Fiset — Binary Trees](https://www.youtube.com/watch?v=BHB0B1jFKQc)

---

## 🧠 Try It Yourself

1. Build the sample tree above and print all three DFS traversals plus the level-order traversal.
2. Implement `height(node)` and `size(node)` and confirm the values by counting on paper.
3. Write `is_full(node)` that checks whether every node has either 0 or 2 children.
4. Write `mirror(node)` that swaps `left` and `right` at every node, turning the tree into its mirror image, and print the inorder traversal before/after to confirm.
