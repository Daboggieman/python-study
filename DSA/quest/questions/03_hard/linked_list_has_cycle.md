# Linked List Has Cycle

Source: linked_list_has_cycle

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Write a function that detects whether a singly linked list contains a cycle, using Floyd's slow/fast pointer technique (constant extra space -- no sets, no id() tracking). Return True if a cycle exists, False otherwise.

Expected function
```python
def has_cycle(head):
    pass
```


Here is a possible program to test your function :
```python
head = build_chain([1, 2, 3, 4])
print(has_cycle(head))

# manually create a cycle: last node points back to the second node
current = head
while current.next:
    current = current.next
second = head.next
current.next = second
print(has_cycle(head))
```

And its output :
```text
False
True
```
