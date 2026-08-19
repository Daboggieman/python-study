# Binary Search First Last Occurrence

Source: binary_search_first_last_occurrence

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Given a sorted list that may contain duplicates, write a function that returns a tuple `(first_index, last_index)` of the first and last occurrence of `target`, both found via binary search (O(log n) each, not a linear scan). Return `(-1, -1)` if `target` isn't present.

Expected function
```python
def first_and_last(arr, target):
    pass
```


Here is a possible program to test your function :
```python
print(first_and_last([1, 2, 2, 2, 3, 4, 5], 2))
print(first_and_last([1, 2, 2, 2, 3, 4, 5], 9))
```

And its output :
```text
(1, 3)
(-1, -1)
```
