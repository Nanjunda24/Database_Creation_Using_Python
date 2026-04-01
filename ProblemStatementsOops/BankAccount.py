class BankAccount:
    def __init__(self,account_no,balance):
        self.account_no = account_no
        self.balance = balance

    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
        else:
            print("The deposition amount should be greater than 0")
    
    def withdraw(self, money):
        if money <= self.balance:
            self.balance -= money
            print(f"Rs.{money}  withdrawal successfully completed collect your amount!!!!!")
        else:
            print("Insufficient balance")
    
    def display_balance(self):

        print("Account balance account ending with ----9780: ",self.balance)

obj = BankAccount(2737469780,100)

obj.deposite(20)

obj.display_balance()

obj.withdraw(450)

obj.display_balance()