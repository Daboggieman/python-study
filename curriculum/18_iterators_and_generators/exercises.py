# Exercise 18: Iterators and Generators
# Run this script with: python exercises.py

import itertools


# TODO: Exercise 1 - iterator class version
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        pass


# TODO: Exercise 1 - generator function version
def countdown(start):
    pass


# TODO: Exercise 2
def fibonacci(n):
    pass


# TODO: Exercise 3 - use a generator expression, not a list comprehension
def sum_of_squares(n):
    pass


if __name__ == "__main__":
    print(list(Countdown(3)))          # [3, 2, 1]
    print(list(countdown(3)))          # [3, 2, 1]
    print(list(fibonacci(8)))           # [0, 1, 1, 2, 3, 5, 8, 13]
    print(sum_of_squares(10))            # 385

    counter = itertools.count(start=1, step=2)
    print([next(counter) for _ in range(5)])   # [1, 3, 5, 7, 9]
