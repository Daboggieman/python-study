# DSA Exercise 06: Hash Tables
# Run this script with: python exercises.py

class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    # TODO: Exercise 1
    def put(self, key, value):
        pass

    # TODO: Exercise 2
    def get(self, key):
        pass

    # TODO: Exercise 3
    def remove(self, key):
        pass


# TODO: Exercise 4
# Return the first character that repeats in `s`, using O(n) time (a set or dict).
# Return None if there are no repeats.
def first_repeated_char(s):
    pass


# TODO: Exercise 5
# Classic "two sum": return a tuple of the two INDICES whose values sum to
# `target`. Must run in O(n) using a dict (not the O(n^2) nested loop).
def two_sum(nums, target):
    pass


if __name__ == "__main__":
    ht = HashTable(capacity=2)   # tiny capacity on purpose, forces collisions
    ht.put("apple", 1.5)
    ht.put("banana", 0.5)
    ht.put("cherry", 3.0)
    print(ht.get("banana"))   # 0.5
    ht.remove("apple")
    try:
        ht.get("apple")
    except KeyError:
        print("apple correctly removed")

    print(first_repeated_char("swiss"))   # s
    print(two_sum([2, 7, 11, 15], 9))      # (0, 1)
