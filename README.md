# python-internship-day10
# Task 10: Object-Oriented Programming (OOP)

##  Overview
This task demonstrates Object-Oriented Programming concepts in Python by simulating real-world bank operations using classes and objects.

##  Tools Used
- Python
- VS Code

##  Files Included
- `bank_account.py` → OOP-based Python program
- `README.md` → Task documentation

## OOP Concepts Implemented

### 1. Class & Constructor
- `BankAccount` and `SavingsAccount`
- `__init__()` used to initialize objects

### 2. Attributes & Methods
- Attributes: account_holder, balance, interest_rate
- Methods: deposit(), withdraw(), get_balance()

### 3. Encapsulation
- Balance protected using `_balance`
- Accessed only through methods

### 4. Inheritance
- `SavingsAccount` inherits from `BankAccount`

### 5. Polymorphism
- `get_balance()` method overridden in `SavingsAccount`

### 6. Multiple Objects
- Created multiple account objects to simulate real users

### 7. Real Bank Operations
- Deposit
- Withdraw
- Balance check with interest

##  Learning Outcome
This task helped me understand software design using OOP concepts and how real-world systems like banks are modeled in Python.

##  How to Run
```bash
python bank_account.py
