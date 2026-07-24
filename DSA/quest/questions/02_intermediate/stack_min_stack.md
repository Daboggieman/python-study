# Stack Min Stack

Source: stack_min_stack

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Design a `MinStack` class that supports `push(x)`, `pop()`, `top()`, and `get_min()`, where `get_min()` returns the minimum element currently in the stack, all in O(1) time. (Hint: keep a second stack that tracks the running minimum alongside the main stack.)

Expected function
```python
class MinStack:
    def __init__(self):
        pass

    def push(self, x):
        pass

    def pop(self):
        pass

    def top(self):
        pass

    def get_min(self):
        pass
```


Here is a possible program to test your function :
```python
ms = MinStack()
ms.push(5)
ms.push(2)
ms.push(7)
print(ms.get_min())
ms.pop()
print(ms.get_min())
print(ms.top())
```

And its output :
```text
2
2
2
```
