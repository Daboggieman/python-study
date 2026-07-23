# DSA Exercise 16: Insertion Sort
# Run this script with: python exercises.py

import bisect
import time


# TODO: Exercise 1
def insertion_sort(arr):
    pass


# TODO: Exercise 2 - use bisect_left to find the insertion point faster
def binary_insertion_sort(arr):
    pass


# TODO: Exercise 3 - time insertion_sort on a sorted vs reverse-sorted list of size n
def compare_best_worst_case(n):
    pass


if __name__ == "__main__":
    print(insertion_sort([5, 2, 4, 1]))          # [1, 2, 4, 5]
    print(binary_insertion_sort([5, 2, 4, 1]))    # [1, 2, 4, 5]
    compare_best_worst_case(5000)
