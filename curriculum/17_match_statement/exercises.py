# Exercise 17: The match Statement
# Run this script with: python exercises.py


# TODO: Exercise 1
def describe_status(code):
    pass


# TODO: Exercise 2
# Handle commands: ["go", direction], ["take", item], ["look"], anything else
def handle_command(command):
    pass


# TODO: Exercise 3 - use guards
def classify(n):
    pass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# TODO: Exercise 4
def describe_point(p):
    pass


if __name__ == "__main__":
    print(describe_status(200))              # OK (or similar)
    print(describe_status(404))              # Not Found (or similar)
    print(handle_command(["go", "north"]))    # Moving north
    print(handle_command(["take", "key"]))     # Taking key
    print(classify(-5))                         # negative
    print(classify(4))                          # positive even
    print(describe_point(Point(0, 0)))          # Origin
