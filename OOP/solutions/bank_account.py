class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self._history = self.history
    history = []
    def deposit(self, amount):
        if amount < 1:
            return "minimum deposit is 1"
        self.balance = self.balance + amount
        return {
            self.balance, 
            f"{amount} has been credited to your account",
            self.history.append(f"Deposited {amount}")        
        }

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Balance"
        elif amount < 1:
            return "minimum withdrawal is 1"
        else:
            self.balance = self.balance - amount
        return {
            self.balance,
            f"{amount} has been withdrawn from your account balance",
            self.history.append(f"Deposited {amount}")
        }    

    def append_json(filepath, record):
        with open(filepath, "a") as f:
            f.write(json.dumps(record) + "\n")

acc = BankAccount("Raph'el", 100)
acc.deposit(50)
acc.withdraw(70)
# print(acc.get_balance())     # 120
# print(acc.get_history())     # ["Deposited 50", "Withdrew 30"]
acc.withdraw(1000)           # raises ValueError
print(acc.history)
print(acc.balance)


acc = BankAccount("Naomi Ogah", 85)
acc.deposit(32)
acc.withdraw(44)
# print(acc.get_balance())     # 120
# print(acc.get_history())     # ["Deposited 50", "Withdrew 30"]
acc.withdraw(1000)           # raises ValueError
print(acc.history)
print(acc.balance)

filepath1 = "/home/student/python-study/OOP/solutions/output.json"