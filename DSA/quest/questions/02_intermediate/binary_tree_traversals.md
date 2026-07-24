# Binary Tree Traversals

Source: binary_tree_traversals

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Given a binary tree (`TreeNode` with `data`, `left`, `right`), write three functions returning lists: `inorder(node)` (Left, Node, Right), `preorder(node)` (Node, Left, Right), and `postorder(node)` (Left, Right, Node).

Expected function
```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(node):
    pass

def preorder(node):
    pass

def postorder(node):
    pass
```


Here is a possible program to test your function :
```python
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(inorder(root))
print(preorder(root))
print(postorder(root))
```

And its output :
```text
[4, 2, 5, 1, 3]
[1, 2, 4, 5, 3]
[4, 5, 2, 3, 1]
```
