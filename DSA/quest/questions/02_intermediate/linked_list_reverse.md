# Linked List Reverse

Source: linked_list_reverse

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Write a function that reverses a singly linked list **iteratively** (no recursion, no converting to a Python list) and returns the new head.

Expected function
```python
def reverse_linked_list(head):
    pass
```


Here is a possible program to test your function :
```python
head = build_chain([1, 2, 3, 4, 5])
new_head = reverse_linked_list(head)
values = []
while new_head:
    values.append(new_head.data)
    new_head = new_head.next
print(values)
```

And its output :
```text
[5, 4, 3, 2, 1]
```
