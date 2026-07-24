# Binary Tree Is Balanced

Source: binary_tree_is_balanced

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Write a function that checks whether a binary tree is height-balanced: for every node, the height difference between its left and right subtrees is at most 1. Aim for an O(n) solution (compute height and balance status together in one pass, rather than recomputing height repeatedly).

Expected function
```python
def is_balanced(root):
    pass
```


Here is a possible program to test your function :
```python
balanced = TreeNode(1)
balanced.left = TreeNode(2)
balanced.right = TreeNode(3)
print(is_balanced(balanced))

unbalanced = TreeNode(1)
unbalanced.left = TreeNode(2)
unbalanced.left.left = TreeNode(3)
unbalanced.left.left.left = TreeNode(4)
print(is_balanced(unbalanced))
```

And its output :
```text
True
False
```
