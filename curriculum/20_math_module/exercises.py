# Exercise 20: The math Module
# Run this script with: python exercises.py

import math
import statistics


# TODO: Exercise 1
def hypotenuse(a, b):
    pass


# TODO: Exercise 3 - only test divisors up to sqrt(n)
def is_prime(n):
    pass


if __name__ == "__main__":
    print(hypotenuse(3, 4))                     # 5.0
    print(math.hypot(3, 4))                       # 5.0 (should match!)

    print(0.1 + 0.2 == 0.3)                        # False
    print(math.isclose(0.1 + 0.2, 0.3))              # True

    print(is_prime(17))                               # True
    print(is_prime(18))                                # False

    data = [2, 4, 4, 4, 5, 5, 7, 9]
    print(statistics.mean(data))
    print(round(statistics.stdev(data), 2))
