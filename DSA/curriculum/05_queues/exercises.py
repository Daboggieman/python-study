# DSA Exercise 05: Queues
# Run this script with: python exercises.py

from collections import deque


class Queue:
    def __init__(self):
        self._items = deque()

    # TODO: Exercise 1
    def enqueue(self, item):
        pass

    # TODO: Exercise 2
    def dequeue(self):
        pass

    # TODO: Exercise 3
    def peek(self):
        pass

    def is_empty(self):
        return len(self._items) == 0


# TODO: Exercise 4
# Implement a fixed-size circular queue backed by a plain Python list of
# size `capacity`. Track front/rear indices manually with modulo arithmetic.
# Raise IndexError on enqueue-when-full or dequeue-when-empty.
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.count = 0

    def enqueue(self, item):
        pass

    def dequeue(self):
        pass


if __name__ == "__main__":
    q = Queue()
    q.enqueue("doc1")
    q.enqueue("doc2")
    q.enqueue("doc3")
    print(q.dequeue())  # doc1
    print(q.dequeue())  # doc2

    cq = CircularQueue(3)
    cq.enqueue("a")
    cq.enqueue("b")
    cq.enqueue("c")
    print(cq.dequeue())  # a
    cq.enqueue("d")       # should reuse freed slot
    print(cq.dequeue())  # b
    print(cq.dequeue())  # c
    print(cq.dequeue())  # d
