# Tree Sum All Values

Source: tree_sum_all_values

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Given a general (N-ary) tree where each `TreeNode` has `data` and a `children` list, write a function that returns the sum of all node values in the tree, using recursion.

Expected function
```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def tree_sum(node):
    pass
```


Here is a possible program to test your function :
```python
root = TreeNode(1)
child_a = TreeNode(2)
child_b = TreeNode(3)
root.children = [child_a, child_b]
child_a.children = [TreeNode(4), TreeNode(5)]
print(tree_sum(root))
```

And its output :
```text
15
```
