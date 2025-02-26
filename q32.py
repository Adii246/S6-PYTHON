'''
Question:

Write a Python class BankAccount with the following methods:

init(self, account_holder, balance=0): Initializes the account with the account holder’s name and an optional balance (default is 0).
deposit(self, amount): Adds the given amount to the account balance.

withdraw(self, amount): Deducts the given amount from the balance if sufficient funds are available; otherwise, prints "Insufficient balance"

display_balance(self): Prints the current balance.

Task:

Create a BankAccount object for a user named "Alice" with an initial balance of 500.

Deposit 200 into Alice's account.

Withdraw 100.

Display the final balance.
'''

class bank_account:
    def __init__(self,account_holder,balance=0):
        self.name=account_holder
        self.b=balance
    def deposit(self,amount):
        self.amount=self.b+amount
        #print("New Balance after depositing:",f"{self.amount}")
    def withdraw(self,amount):
        self.amount=self.amount-amount
        #print("New Balance after withdrawing:",f"{self.amount}")      
    def display_balance(self):
        print("Account_holder:",f"{self.name}\n","Balance:",f"{self.amount}")

b1=bank_account("Alice",500)
b1.deposit(200)
b1.withdraw(100)
b1.display_balance()
