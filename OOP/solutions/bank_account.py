import json
import os


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount < 1:
            return "minimum deposit is 1"
        self.balance += amount
        self.history.append(f"Deposited {amount}")
        return {
            "name": self.name,
            "action": "deposit",
            "amount": amount,
            "balance": self.balance,
            "message": f"{amount} has been credited to your account"
        }

    def withdraw(self, amount):
        if amount < 1:
            return "minimum withdrawal is 1"
        if amount > self.balance:
            return "Insufficient Balance"
        self.balance -= amount
        self.history.append(f"Withdrew {amount}")
        return {
            "name": self.name,
            "action": "withdraw",
            "amount": amount,
            "balance": self.balance,
            "message": f"{amount} has been withdrawn from your account balance"
        }

    def get_balance(self):
        return self.balance

    def get_history(self):
        return self.history


def append_json(filepath, record):
    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(record)

    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)


filepath1 = "/home/student/python-study/OOP/solutions/output.json"

acc = BankAccount("Raph'el", 100)
result = acc.deposit(50)
append_json(filepath1, result)

result = acc.withdraw(70)
append_json(filepath1, result)

print(acc.get_balance())     
print(acc.get_history())     
result = acc.withdraw(1000)
print(result)


acc2 = BankAccount("Naomi Ogah", 85)
result = acc2.deposit(32)
append_json(filepath1, result)

result = acc2.withdraw(44)
append_json(filepath1, result)

print(acc2.get_balance())  
print(acc2.get_history())