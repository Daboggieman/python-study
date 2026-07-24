# DSA Exercise 02: Nodes
# Run this script with: python exercises.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# TODO: Exercise 1
# Manually create 4 nodes holding the values 10, 20, 30, 40 and link them
# together in order (10 -> 20 -> 30 -> 40 -> None).
def build_chain():
    pass


# TODO: Exercise 2
# Write a function that counts how many nodes are in a chain starting at `head`.
def count_nodes(head):
    pass


# TODO: Exercise 3
# Write a function that returns the sum of all `.data` values in a chain
# of nodes (assume all data is numeric).
def sum_chain(head):
    pass


# TODO: Exercise 4
# Write a function that returns True if `target` value exists anywhere
# in the chain, False otherwise. Do NOT use a Python list.
def contains(head, target):
    pass


if __name__ == "__main__":
    head = build_chain()
    print(count_nodes(head))   # 4
    print(sum_chain(head))     # 100
    print(contains(head, 30))  # True
    print(contains(head, 99))  # False
