# DSA Exercise 04: Stacks
# Run this script with: python exercises.py

class Stack:
    def __init__(self):
        self._items = []

    # TODO: Exercise 1
    def push(self, item):
        pass

    # TODO: Exercise 2
    def pop(self):
        pass

    # TODO: Exercise 3
    def peek(self):
        pass

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)


# TODO: Exercise 4
# Use a Stack to determine whether brackets in `expression` are balanced.
# Supported bracket types: (), [], {}
def is_balanced(expression):
    pass


# TODO: Exercise 5
# Use a Stack to reverse a string (do not use slicing or reversed()).
def reverse_string(s):
    pass


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.peek())   # 3
    print(s.pop())     # 3
    print(s.size())    # 2

    print(is_balanced("{[()()]}"))  # True
    print(is_balanced("{[(])}"))    # False

    print(reverse_string("hello"))  # olleh
