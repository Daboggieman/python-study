# Queue Circular Buffer

Source: queue_circular_buffer

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Implement a fixed-size `CircularQueue` backed by a plain Python list of size `capacity` (not `collections.deque`). Support `enqueue(x)` (raise `IndexError` if full), `dequeue()` (raise `IndexError` if empty, else remove and return the front item), and `is_full()` / `is_empty()`. Use modulo arithmetic to wrap indices instead of shifting elements.

Expected function
```python
class CircularQueue:
    def __init__(self, capacity):
        pass

    def enqueue(self, item):
        pass

    def dequeue(self):
        pass

    def is_full(self):
        pass

    def is_empty(self):
        pass
```


Here is a possible program to test your function :
```python
cq = CircularQueue(3)
cq.enqueue("a")
cq.enqueue("b")
cq.enqueue("c")
print(cq.is_full())
print(cq.dequeue())
cq.enqueue("d")
print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())
```

And its output :
```text
True
a
b
c
d
```
