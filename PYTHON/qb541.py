class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance
    def Deposite(self,amount):
        self.balance+=amount
    def Withdraw(self,amount):
        if (amount<self.balance):
            self.balance-=amount
    def Display(self):
        return self.accountNumber,self.name,self.balance
s=BankAccount(78564121,"ds",7777777)
