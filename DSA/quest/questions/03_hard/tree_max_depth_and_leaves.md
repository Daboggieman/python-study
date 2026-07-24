# Tree Max Depth And Leaves

Source: tree_max_depth_and_leaves

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Given a general (N-ary) tree, write two functions: `tree_height(node)` returning the height (longest root-to-leaf path in edges; a single node has height 0), and `count_leaves(node)` returning how many leaf nodes (no children) exist.

Expected function
```python
def tree_height(node):
    pass

def count_leaves(node):
    pass
```


Here is a possible program to test your function :
```python
root = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
root.children = [b, c]
b.children = [TreeNode("D"), TreeNode("E")]
print(tree_height(root))
print(count_leaves(root))
```

And its output :
```text
2
3
```
