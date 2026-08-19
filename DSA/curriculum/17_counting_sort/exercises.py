# DSA Exercise 17: Counting Sort
# Run this script with: python exercises.py

import time


# TODO: Exercise 1
def counting_sort(arr):
    pass


# TODO: Exercise 2 - sort a list of (score, name) tuples by score only,
# keeping it stable (equal scores preserve original relative order)
def counting_sort_by_key(items, key=lambda x: x[0]):
    pass


if __name__ == "__main__":
    print(counting_sort([4, 2, 2, 8, 3, 3, 1]))  # [1, 2, 2, 3, 3, 4, 8]

    students = [(85, "Bob"), (90, "Ada"), (85, "Amy"), (70, "Cy")]
    print(counting_sort_by_key(students))
    # (85, "Bob") should still come before (85, "Amy") -- stability check
