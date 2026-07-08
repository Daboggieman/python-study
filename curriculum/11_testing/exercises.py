# Exercise 11: Testing
# Run this script with: python exercises.py

import unittest

# Below is the function we want to test:
def add_numbers(a, b):
    """Adds two numbers together. Returns None if inputs are not numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None
    return a + b


# TODO: Write a TestCase class named 'TestAddNumbers' inheriting from 'unittest.TestCase'.
# Add at least three test methods:
# 1. test_positive_numbers: assert equal add_numbers(2, 3) and 5.
# 2. test_negative_numbers: assert equal add_numbers(-1, -1) and -2.
# 3. test_invalid_input: assert equal add_numbers("2", 3) and None.

# To run tests if this file is executed:
if __name__ == '__main__':
    unittest.main()

