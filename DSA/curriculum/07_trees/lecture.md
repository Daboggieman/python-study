# DSA 07: Trees (General Concepts)

A **tree** is a hierarchical data structure made of nodes, where each node has exactly one parent (except the root, which has none) and any number of children. Trees model anything with a natural hierarchy: file systems, org charts, HTML/DOM, decision trees, and more.

---

## 1. Vocabulary You Must Know

| Term | Meaning |
|---|---|
| **Root** | The top node, with no parent |
| **Parent / Child** | A node directly above/below another |
| **Leaf** | A node with no children |
| **Edge** | The connection between a parent and a child |
| **Depth** of a node | Number of edges from the root to that node |
| **Height** of a tree | Number of edges on the longest path from root to a leaf |
| **Subtree** | A node and all of its descendants, treated as its own tree |
| **Degree** | The number of children a node has |

```
        A            <- root, depth 0
       / \
      B   C           <- depth 1
     /|    \
    D E     F         <- depth 2 (D, E, F are leaves)
```
Height of this tree = 2.

---

## 2. A Generic (N-ary) Tree Node

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []      # any number of children

    def add_child(self, child_node):
        self.children.append(child_node)
```

```python
root = TreeNode("CEO")
vp_eng = TreeNode("VP Engineering")
vp_sales = TreeNode("VP Sales")
root.add_child(vp_eng)
root.add_child(vp_sales)
vp_eng.add_child(TreeNode("Engineer A"))
vp_eng.add_child(TreeNode("Engineer B"))
```

---

## 3. Traversal Strategies

There are two big families of traversal:

### Depth-First (go as deep as possible before backtracking) — usually recursive, uses a stack (or the call stack)
```python
def dfs(node, depth=0):
    print("  " * depth + str(node.data))
    for child in node.children:
        dfs(child, depth + 1)
```

### Breadth-First (visit level by level) — uses a queue
```python
from collections import deque

def bfs(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data)
        for child in node.children:
            queue.append(child)
```

---

## 4. Why Trees Matter

- File systems are trees (folders contain files/folders).
- The DOM (web pages) is a tree.
- Decision trees in machine learning.
- Parsing (abstract syntax trees for compilers/interpreters).
- Binary search trees, heaps, tries — all specialized trees covered in upcoming lessons.

---

## 📚 Resources

- **W3Schools:** [DSA Trees](https://www.w3schools.com/dsa/dsa_data_trees.php)
- **YouTube:** [mycodeschool — Introduction to Trees](https://www.youtube.com/watch?v=qH6yxkw0u78)
- **YouTube:** [Abdul Bari — Tree Data Structure](https://www.youtube.com/watch?v=oSWTXtMglKE)

---

## 🧠 Try It Yourself

1. Build the CEO/VP org-chart tree above and write a `dfs` that prints it indented by depth (as shown).
2. Write a `bfs` that prints the tree level by level.
3. Write a function `tree_height(node)` that returns the height of a general (N-ary) tree.
4. Write a function `count_leaves(node)` that counts how many leaf nodes exist in the tree.
