# AVL Delete With Rebalance

Source: avl_delete_with_rebalance

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Implement AVL tree **deletion**. This is the hardest exercise in the module: perform a standard BST delete (leaf, one-child, or two-children/in-order-successor cases), then walk back up updating heights and applying the same four rotation cases used in insertion to restore balance. The tree must remain a valid, height-balanced BST after every deletion.

Expected function
```python
def delete(node, value):
    pass
```


Here is a possible program to test your function :
```python
root = None
for value in [10, 20, 30, 40, 50, 25]:
    root = insert(root, value)
print(get_height(root))

root = delete(root, 30)
root = delete(root, 40)
print(get_height(root))
```

And its output :
```text
2
2
```
