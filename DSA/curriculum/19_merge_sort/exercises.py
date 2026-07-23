# DSA Exercise 19: Merge Sort
# Run this script with: python exercises.py

import time
import sys

sys.setrecursionlimit(10000)


# TODO: Exercise 1
def merge(left, right):
    pass


# TODO: Exercise 2
def merge_sort(arr):
    pass


# TODO: Exercise 3 - count inversions (pairs i < j where arr[i] > arr[j])
# while merge-sorting, returning (sorted_list, inversion_count)
def merge_sort_count_inversions(arr):
    pass


if __name__ == "__main__":
    print(merge_sort([5, 2, 4, 1]))              # [1, 2, 4, 5]
    print(merge_sort_count_inversions([2, 4, 1, 3, 5]))  # (sorted list, 3)
