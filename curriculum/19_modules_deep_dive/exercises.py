# Exercise 19: Modules Deep Dive
# Run this script with: python exercises.py

import sys


# TODO: Exercise 2
# Print the first 3 entries of sys.path
def show_first_three_paths():
    pass


# TODO: Exercise 1 (conceptual, no code needed here -- see instructions.md)
# Create a separate file `mathutils_demo.py` in this folder with:
#   def square(x): return x * x
#   if __name__ == "__main__":
#       print("running directly!")
#       print(square(4))
# Then import it below and confirm the "running directly!" line does NOT print.


if __name__ == "__main__":
    show_first_three_paths()
    print(f"This file's __name__ is: {__name__}")
