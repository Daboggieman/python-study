# AVL Insert And Balance

Source: avl_insert_and_balance

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Implement AVL tree insertion with all four rebalancing cases (Left-Left, Right-Right, Left-Right, Right-Left), so the tree height never exceeds O(log n). Each `AVLNode` tracks its own `height`.

Expected function
```python
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def insert(node, value):
    pass

def get_height(node):
    return node.height if node else 0
```


Here is a possible program to test your function :
```python
root = None
for value in [1, 2, 3, 4, 5, 6, 7]:
    root = insert(root, value)
print(get_height(root))
```

And its output :
```text
2
```
