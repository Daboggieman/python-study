# List Reverse Inplace

Source: list_reverse_inplace

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Write a function that reverses a list **in place** (modifying the original list) without using slicing (`[::-1]`), `reversed()`, or `.reverse()`. Use a two-pointer swap instead. The function should return the same list object, now reversed.

Expected function
```python
def list_reverse_inplace(arr):
    pass
```


Here is a possible program to test your function :
```python
nums = [1, 2, 3, 4, 5]
print(list_reverse_inplace(nums))
print(nums)
```

And its output :
```text
[5, 4, 3, 2, 1]
[5, 4, 3, 2, 1]
```
