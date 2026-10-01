class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount

    def __repr__(self):
        return f"BankAccount(balance={self.balance})"


account = BankAccount(100)
print(account)          # BankAccount(balance=100)

account.deposit(50)
print(account.balance)  # 150

account.withdraw(20)
print(account.balance)  # 130