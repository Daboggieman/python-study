# BST Validate

Source: bst_validate

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Write a function that checks whether a given binary tree is a valid Binary Search Tree. Every node's value must be strictly greater than every value in its left subtree and strictly less than every value in its right subtree (not just compared to its immediate children).

Expected function
```python
def is_valid_bst(root):
    pass
```


Here is a possible program to test your function :
```python
valid = TreeNode(5)
valid.left = TreeNode(3)
valid.right = TreeNode(8)
print(is_valid_bst(valid))

invalid = TreeNode(5)
invalid.left = TreeNode(3)
invalid.right = TreeNode(8)
invalid.right.left = TreeNode(4)   # 4 < 5 but sits in the right subtree -- invalid!
print(is_valid_bst(invalid))
```

And its output :
```text
True
False
```
