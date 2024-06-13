class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount 
        self.name = acctName 
        print(f"\nAccount '{self.name}' created. \nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"Account '{self.name}' balance = {self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount 
        print("\nDeposit complete")
        self.getBalance()
    
    def viableTransaction(self, amount):
        if amount > self.balance:
            raise BalanceException(f"\nSorry, account '{self.name} only has a balance of ${self.balance:.2f}...") 
        else:
            return 

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount 
            print("\nWithdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw failed: {error}")

    def transfer(self, amount, reciever):
        try:
            print("\n**********\n\nTransferint....🚀")
            self.viableTransaction(amount)
            self.withdraw(amount) 
            reciever.deposit(amount)
            print("\nTransfer complete!✅\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer failed: ❌ {error}\n\n**********")


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + amount * 1.05
        print("\nDeposit complete")
        self.getBalance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName) 
        self.fee = 5


    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balace = self.balance = amount - self.fee
            print("\nWithdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw failed: {error}")
