# Selection Sort Kth Largest

Source: selection_sort_kth_largest

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Using the selection-sort idea (repeatedly select the largest remaining element) but stopping after `k` selections instead of sorting the whole array, write a function that returns the k-th largest value in `arr` (1-indexed: k=1 means the largest). Do not use `sorted()` or `.sort()`.

Expected function
```python
def kth_largest(arr, k):
    pass
```


Here is a possible program to test your function :
```python
print(kth_largest([3, 2, 1, 5, 6, 4], 2))
```

And its output :
```text
5
```
