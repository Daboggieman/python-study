# BST Kth Smallest

Source: bst_kth_smallest

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Write a function that returns the k-th smallest value (1-indexed) in a Binary Search Tree, using an in-order traversal that stops early once the k-th element is found (don't build the full sorted list if you can avoid it, though a full in-order list is also acceptable for correctness).

Expected function
```python
def kth_smallest(root, k):
    pass
```


Here is a possible program to test your function :
```python
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
print(kth_smallest(root, 3))
```

And its output :
```text
6
```
