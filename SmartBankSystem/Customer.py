class Customer:
    def __init__(self,customerID,CustomerName,accountNumber,balance):
        self.__customerID = customerID
        self.__customerName = CustomerName
        self.__accountNumber = accountNumber
        self.__balance = balance


        def setcustomerID(self):
            self.__customerID = customerID

        def setCustomerName(self,name):
            self.__customerName = name 

        def setAccountNumber(self,accountNumber):
            self.__accountNumber = accountNumber

        def setBalance(self,balance):
            self.__balance = balance

        def getCustomerID(self):
            return self.__customerID

        def getCustomerName(self):
            return self.__customerName
        
        def getAccountNumber(self):
            return self.__accountNumber
        
        def getAccountBalance(self):
            return self.__balance
        
from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self, Customer):
        self.Customer = Customer

        def deposite(self,amount):
            if amount > 0:
                balance = self.Customer.getAccountBalance() + amount
                print("Amount deposited successfully!!! New Balance:", self.Customer.getAccountBalance())
                self.Customer.setBalance(balance)
            else:
                print("Amount should be greater than zero to deposit.")
    
    def displayBalance(self):
        print(:"Account balnce is : "+ )
