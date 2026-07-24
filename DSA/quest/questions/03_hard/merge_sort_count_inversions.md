# Merge Sort Count Inversions

Source: merge_sort_count_inversions

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
An inversion is a pair of indices `(i, j)` with `i < j` and `arr[i] > arr[j]`. Write a function that sorts `arr` using merge sort AND counts the total number of inversions, all in O(n log n) time (the count must be produced as a side effect of merging, not with a separate O(n^2) nested loop). Return a tuple `(sorted_list, inversion_count)`.

Expected function
```python
def merge_sort_count_inversions(arr):
    pass
```


Here is a possible program to test your function :
```python
print(merge_sort_count_inversions([2, 4, 1, 3, 5]))
```

And its output :
```text
([1, 2, 3, 4, 5], 3)
```
