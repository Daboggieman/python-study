# Node Chain Max Value

Source: node_chain_max_value

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Write a function that finds the maximum numeric value in a chain of nodes, and a second function that counts how many times a target value occurs in the chain. Do not convert the chain into a Python list.

Expected function
```python
def chain_max(head):
    pass

def chain_count_value(head, target):
    pass
```


Here is a possible program to test your function :
```python
head = build_chain([4, 9, 2, 9, 7])
print(chain_max(head))
print(chain_count_value(head, 9))
```

And its output :
```text
9
2
```
