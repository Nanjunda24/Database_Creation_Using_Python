# 1. Constructor & Methods

#    Create a class BankAccount with:

#    attributes: account_number, balance

#   methods: deposit(amount), withdraw(amount), and display_balance()

#   Ensure that withdrawal does not allow the balance to go below 0.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if isinstance (amount,int):
            if amount > 0:
                self.balance += amount
                print(f"Deposited {amount}, New Balance: {self.balance}")
            else:
                print("Amont should be greater than 0 ")
        else:
            print("AMount should be integer number")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} Successful!!!, Remaining Balance: {self.balance}")

    def display_balance(self):
        print(f"Account {self.account_number} Balance: {self.balance}")


# Example
acc1 = BankAccount(12345, 1000)
acc1.deposit(500)
acc1.withdraw(200)
acc1.withdraw(2000)
acc1.display_balance()
