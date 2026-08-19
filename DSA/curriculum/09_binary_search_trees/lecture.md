# DSA 09: Binary Search Trees (BST)

A **Binary Search Tree** is a binary tree with one extra rule that makes searching fast:

> For every node: everything in its **left** subtree is **smaller**, and everything in its **right** subtree is **larger**.

This single rule turns a tree into something you can binary-search, just like a sorted list — except insertion and deletion stay fast too.

---

## 1. The Node (same shape as a binary tree)

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

```
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
```
Notice: everything left of 8 is < 8, everything right of 8 is > 8, and the same holds recursively at every node.

---

## 2. Insertion

```python
def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.data:
        root.left = insert(root.left, value)
    elif value > root.data:
        root.right = insert(root.right, value)
    # if value == root.data: typically ignore duplicates
    return root
```

---

## 3. Searching

```python
def search(root, target):
    if root is None:
        return False
    if root.data == target:
        return True
    if target < root.data:
        return search(root.left, target)
    return search(root.right, target)
```

Because at each step you eliminate one whole subtree, search is **O(h)** where `h` is the tree's height. For a *balanced* BST, `h = O(log n)`. But for an unlucky/unbalanced BST (e.g., inserting sorted data 1,2,3,4,5...), the tree degenerates into a straight line and `h = O(n)` — no better than a linked list! (This is exactly the problem **AVL trees**, next lesson, solve.)

---

## 4. Deletion (the trickiest BST operation)

Three cases:
1. **Node is a leaf** → just remove it.
2. **Node has one child** → replace the node with its child.
3. **Node has two children** → replace the node's value with its **in-order successor** (the smallest value in its right subtree), then delete that successor from the right subtree.

```python
def find_min(node):
    while node.left:
        node = node.left
    return node

def delete(root, value):
    if root is None:
        return None
    if value < root.data:
        root.left = delete(root.left, value)
    elif value > root.data:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        successor = find_min(root.right)
        root.data = successor.data
        root.right = delete(root.right, successor.data)
    return root
```

---

## 5. In-Order Traversal Gives You Sorted Order (for free!)

This is the "party trick" of a BST — traverse it in-order and you get every value in sorted order, no separate sort needed.

```python
def inorder(node, result=None):
    if result is None:
        result = []
    if node:
        inorder(node.left, result)
        result.append(node.data)
        inorder(node.right, result)
    return result
```

---

## 6. Complexity Table

| Operation | Balanced BST | Unbalanced (worst case) |
|---|---|---|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |

---

## 📚 Resources

- **W3Schools:** [DSA Binary Search Trees](https://www.w3schools.com/dsa/dsa_data_binarysearchtrees.php)
- **YouTube:** [mycodeschool — Binary Search Tree Insertion/Deletion](https://www.youtube.com/watch?v=COZK7NATh4k)
- **YouTube:** [Abdul Bari — Binary Search Tree](https://www.youtube.com/watch?v=9Jry5-82I68)

---

## 🧠 Try It Yourself

1. Build the sample tree above through repeated `insert()` calls (start from an empty tree), then confirm `inorder()` returns a sorted list.
2. Implement `search()` and test both a value that exists and one that doesn't.
3. Implement `delete()` and test all three deletion cases (leaf, one child, two children).
4. Insert the sorted sequence `1, 2, 3, 4, 5` one at a time and print the tree's height. Compare it to inserting `3, 1, 4, 5, 2` — same 5 values, very different height. This is exactly the motivation for the next lesson.
