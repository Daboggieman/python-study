# DSA Exercise 01: Lists (Dynamic Arrays)
# Run this script with: python exercises.py

import time

# TODO: Exercise 1
# Write a function 'time_append' that appends `n` integers to a list using
# .append() and returns the elapsed time in seconds.
def time_append(n):
    pass


# TODO: Exercise 2
# Write a function 'time_insert_front' that inserts `n` integers at index 0
# using .insert(0, x) and returns the elapsed time in seconds.
def time_insert_front(n):
    pass


# TODO: Exercise 3
# Implement a two-pointer palindrome checker (no reversing, no slicing).
def is_palindrome(s):
    pass


# TODO: Exercise 4
# Implement a fixed-size sliding window that returns the maximum sum of any
# contiguous subarray of length k.
def max_sum_subarray(nums, k):
    pass


# TODO: Exercise 5
# Without running it, predict (as a comment) the time complexity of the
# function below, then run it to see if larger inputs behave as predicted.
def mystery(nums):
    total = 0
    for x in nums:
        if x in nums:      # <-- think carefully about this line
            total += 1
    return total


if __name__ == "__main__":
    print("Append 100,000 items:", time_append(100_000))
    print("Insert-at-front 20,000 items:", time_insert_front(20_000))
    print(is_palindrome("racecar"))          # True
    print(is_palindrome("hello"))            # False
    print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # 9
