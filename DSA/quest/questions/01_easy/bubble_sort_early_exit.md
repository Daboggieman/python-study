# Bubble Sort Early Exit

Source: bubble_sort_early_exit

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Implement an optimized bubble sort that stops early if a full pass makes zero swaps (best case O(n) for already-sorted input). Return a tuple of `(sorted_list, number_of_passes)`.

Expected function
```python
def bubble_sort_optimized(arr):
    pass
```


Here is a possible program to test your function :
```python
print(bubble_sort_optimized([1, 2, 3, 4, 5]))
print(bubble_sort_optimized([5, 4, 3, 2, 1]))
```

And its output :
```text
([1, 2, 3, 4, 5], 1)
([1, 2, 3, 4, 5], 4)
```
