class Bank:
    def __init__(self,acc_no,name,balalce):
        self.acc_no = acc_no
        self.name = name
        self.balance = balalce
    def check_balance(self):
        print("Account balance: ",self.balance)
    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            print("Account balance after deposition: ",self.balance)
        else:  
            print("Deposition amount should be positive !!!")
    def withdraw(self , amount):
        if amount > 0 and amount < self.balance:
            self.balance -= amount
            print("Withdraw successfully completed !!!!")
            print("Account balance after withdraw : ",self.balance)
        else:
            print("Insufficient balance!!!!!")


bank = Bank(73090100045714,"Nanjunda K M",1000)

# bank.check_balance()

# bank.deposite(8999)

# bank.withdraw(100)
# bank.deposite(-98)
while True:
    print("----------------Banking System-----------------")
    print("1. Check balance ")
    print("2. Deposite amount ")
    print("3. Withdraw amount ")
    print("4. Exite ")

    choice = int(input("Enter your choice: "))

    if choice==1:
        bank.check_balance()
    elif choice==2:
        amount = int(input("Enter amount to deposite: "))
        bank.deposite(amount)
    elif choice==3:
        amount = int(input("Enter amount to withdraw  your  money: "))
        bank.withdraw(amount)
    elif choice==4:
        print("Exited Successfully!!!!")
        break
    else:
        print("You are entered invalid choice!!!!")

