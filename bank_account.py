# TASK 10: Object-Oriented Programming (OOP)

# Base class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        # Encapsulation (protected attribute)
        self.account_holder = account_holder
        self._balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{amount} deposited successfully")
        else:
            print("Invalid deposit amount")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"{amount} withdrawn successfully")
        else:
            print("Insufficient balance")

    # Method to check balance
    def get_balance(self):
        return self._balance


# Child class (Inheritance)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    # Method overriding (Polymorphism)
    def get_balance(self):
        interest = self._balance * self.interest_rate
        return self._balance + interest


# Creating multiple objects
account1 = BankAccount("Alice", 1000)
account2 = SavingsAccount("Bob", 2000)

# Simulating bank operations
print("\n--- Bank Account Operations ---")
account1.deposit(500)
account1.withdraw(300)
print("Alice Balance:", account1.get_balance())

print("\n--- Savings Account Operations ---")
account2.deposit(1000)
account2.withdraw(500)
print("Bob Balance with Interest:", account2.get_balance())
