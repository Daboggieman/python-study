# List Rotate K

Source: list_rotate_k

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Write a function that rotates a list to the right by `k` positions, in place, without using slicing to build a new list (you may use at most O(1) extra temporary variables, not a second full-size list). Handle `k` larger than the list length by taking `k % len(arr)`.

Expected function
```python
def list_rotate_k(arr, k):
    pass
```


Here is a possible program to test your function :
```python
nums = [1, 2, 3, 4, 5, 6, 7]
print(list_rotate_k(nums, 3))
```

And its output :
```text
[5, 6, 7, 1, 2, 3, 4]
```
