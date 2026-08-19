# DSA Exercise 03: Linked Lists
# Run this script with: python exercises.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # TODO: Exercise 1 - insert a new node at the front, O(1)
    def push_front(self, data):
        pass

    # TODO: Exercise 2 - insert a new node at the back, O(n) is fine here
    def push_back(self, data):
        pass

    # TODO: Exercise 3 - remove and return the value at the front, or None if empty
    def pop_front(self):
        pass

    # TODO: Exercise 4 - return the middle node's data using slow/fast pointers
    def find_middle(self):
        pass

    # TODO: Exercise 5 - reverse the list in place (iterative, O(n), O(1) extra space)
    def reverse(self):
        pass

    def display(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        print(" -> ".join(values) if values else "EMPTY")


if __name__ == "__main__":
    ll = LinkedList()
    for value in [3, 2, 1]:
        ll.push_front(value)     # expect 1 -> 2 -> 3
    ll.push_back(4)               # expect 1 -> 2 -> 3 -> 4
    ll.display()
    print(ll.find_middle())       # expect 2 or 3 depending on convention
    ll.reverse()
    ll.display()                  # expect reversed order
    print(ll.pop_front())
    ll.display()
