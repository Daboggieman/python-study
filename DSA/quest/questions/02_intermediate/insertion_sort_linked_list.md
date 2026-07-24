# Insertion Sort Linked List

Source: insertion_sort_linked_list

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Implement insertion sort directly on a singly linked list (not by converting it to a Python list and back). Build a new sorted chain by repeatedly removing the head of the input list and inserting it into the correct position of the sorted chain. Return the new sorted head.

Expected function
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertion_sort_list(head):
    pass
```


Here is a possible program to test your function :
```python
def build_chain(values):
    dummy = Node(None)
    current = dummy
    for v in values:
        current.next = Node(v)
        current = current.next
    return dummy.next

def to_list(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result

head = build_chain([4, 2, 1, 3])
sorted_head = insertion_sort_list(head)
print(to_list(sorted_head))
```

And its output :
```text
[1, 2, 3, 4]
```
