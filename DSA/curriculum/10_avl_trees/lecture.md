# DSA 10: AVL Trees (Self-Balancing BSTs)

The previous lesson ended on a cliffhanger: a plain BST can degenerate into a straight line (O(n) height) if you insert data in sorted order. An **AVL tree** (named after inventors Adelson-Velsky and Landis) fixes this by automatically rebalancing itself after every insertion/deletion, **guaranteeing** O(log n) height at all times.

---

## 1. The Balance Factor

Every node tracks its own `height`. The **balance factor** of a node is:

```
balance_factor = height(left subtree) - height(right subtree)
```

An AVL tree requires that **every node's balance factor is -1, 0, or 1**. If an insertion/deletion pushes any node outside that range, the tree performs a **rotation** to fix it.

```python
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1     # height of subtree rooted here (leaf = 1)
```

---

## 2. Helper Functions

```python
def get_height(node):
    return node.height if node else 0

def get_balance(node):
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)
```

---

## 3. The Four Rotation Cases

When a node becomes unbalanced, there are exactly four possible shapes, each with its own fix:

| Case | Shape | Fix |
|---|---|---|
| Left-Left (LL) | heavy on left, then left again | single **right rotation** |
| Right-Right (RR) | heavy on right, then right again | single **left rotation** |
| Left-Right (LR) | heavy on left, then right | left rotation on child, then right rotation |
| Right-Left (RL) | heavy on right, then left | right rotation on child, then left rotation |

### Right Rotation (fixes Left-Left)
```python
def rotate_right(y):
    x = y.left
    T2 = x.right

    # perform rotation
    x.right = y
    y.left = T2

    # update heights (order matters: y first, since it's now lower)
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x   # new subtree root
```

### Left Rotation (fixes Right-Right)
```python
def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y
```

---

## 4. Insertion With Rebalancing

```python
def insert(node, value):
    # 1. normal BST insertion
    if node is None:
        return AVLNode(value)
    if value < node.data:
        node.left = insert(node.left, value)
    elif value > node.data:
        node.right = insert(node.right, value)
    else:
        return node  # no duplicates

    # 2. update this node's height
    node.height = 1 + max(get_height(node.left), get_height(node.right))

    # 3. check the balance factor
    balance = get_balance(node)

    # 4. rebalance if needed (4 cases)
    if balance > 1 and value < node.left.data:        # Left-Left
        return rotate_right(node)
    if balance < -1 and value > node.right.data:       # Right-Right
        return rotate_left(node)
    if balance > 1 and value > node.left.data:         # Left-Right
        node.left = rotate_left(node.left)
        return rotate_right(node)
    if balance < -1 and value < node.right.data:       # Right-Left
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node
```

---

## 5. Why Bother?

| | Plain BST (worst case) | AVL Tree (always) |
|---|---|---|
| Search | O(n) | O(log n) |
| Insert | O(n) | O(log n) |
| Delete | O(n) | O(log n) |

The cost: every insert/delete does a *small* amount of extra bookkeeping (updating heights, checking balance, maybe rotating). That small constant overhead buys you a **guarantee** that never degrades, which is why AVL trees (and their cousin, Red-Black trees) power real-world systems like database indexes and language runtime libraries.

---

## 📚 Resources

- **W3Schools:** [DSA AVL Trees](https://www.w3schools.com/dsa/dsa_data_avltrees.php)
- **YouTube:** [mycodeschool — AVL Tree Insertion](https://www.youtube.com/watch?v=jDM6_TnYIqE)
- **YouTube:** [Abdul Bari — AVL Tree](https://www.youtube.com/watch?v=jDM6_TnYIqE)
- **GeeksforGeeks:** [AVL Tree | Set 1 (Insertion)](https://www.geeksforgeeks.org/avl-tree-set-1-insertion/)

---

## 🧠 Try It Yourself

1. Implement `rotate_left` and `rotate_right`, and trace one rotation by hand on paper before running any code.
2. Implement `insert()` with all four rebalancing cases, then insert `1, 2, 3, 4, 5, 6, 7` (sorted order — the BST killer from last lesson) and print the resulting height. It should be much shorter than 6!
3. Add an `inorder()` traversal and confirm the AVL tree still returns sorted order (rotations preserve the BST property).
4. (Challenge) Implement deletion with rebalancing — it's the same idea as insertion's rebalancing, just triggered after a standard BST delete.
