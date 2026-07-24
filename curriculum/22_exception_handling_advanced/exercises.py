# Exercise 22: Exception Handling, Advanced
# Run this script with: python exercises.py


# TODO: Exercise 1 - use try/except/else/finally
def divide(a, b):
    pass


# TODO: Exercise 3
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        pass


# TODO: Exercise 3
def withdraw(balance, amount):
    pass


if __name__ == "__main__":
    print(divide(10, 2))
    print(divide(10, 0))

    try:
        withdraw(100, 500)
    except InsufficientFundsError as e:
        print(f"Error: {e}")
        print(f"Shortfall: {e.amount - e.balance}")
