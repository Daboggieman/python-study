# Node Chain Build And Count

Source: node_chain_build_and_count

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Given a `Node` class with `data` and `next` attributes, write a function that builds a chain of nodes from a Python list of values (returning the `head` node), and a second function that counts how many nodes are in a chain.

Expected function
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def build_chain(values):
    pass

def count_nodes(head):
    pass
```


Here is a possible program to test your function :
```python
head = build_chain([10, 20, 30, 40])
print(count_nodes(head))
```

And its output :
```text
4
```
