# DSA Exercise 12: Linear Search
# Run this script with: python exercises.py

import time


# TODO: Exercise 1
def linear_search(arr, target):
    pass


# TODO: Exercise 2
def find_all(arr, target):
    pass


# TODO: Exercise 3
# Reuse the LinkedList/Node classes from Lesson 03 (rewritten here for
# convenience) and implement linear search over a chain of nodes instead
# of a Python list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def linear_search_linked_list(head, target):
    pass


if __name__ == "__main__":
    data = list(range(1000))
    print(linear_search(data, 500))   # 500
    print(linear_search(data, 9999))  # -1
    print(find_all([1, 2, 3, 2, 1], 2))  # [1, 3]

    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n1.next = n2
    n2.next = n3
    print(linear_search_linked_list(n1, 20))  # True
    print(linear_search_linked_list(n1, 99))  # False
