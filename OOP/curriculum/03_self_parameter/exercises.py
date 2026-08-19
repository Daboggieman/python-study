# OOP Exercise 03: The self Parameter
# Run this script with: python exercises.py


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # TODO: Exercise 2
    def deposit(self, amount):
        pass

    # TODO: Exercise 2
    def withdraw(self, amount):
        pass

    # TODO: Exercise 2
    def print_balance(self):
        pass

    # TODO: Exercise 4
    def transfer(self, other_account, amount):
        pass


if __name__ == "__main__":
    acc1 = BankAccount("Alice", 100)
    acc2 = BankAccount("Bob", 50)

    acc1.deposit(50)
    acc1.print_balance()    # Alice's balance: 150

    acc1.transfer(acc2, 100)
    acc1.print_balance()    # Alice's balance: 50
    acc2.print_balance()    # Bob's balance: 150
