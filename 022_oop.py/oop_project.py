from bank_account import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

# Sara.deposit(800)

Sara.transfer(100, Dave)

Jim = InterestRewardsAcct(1000, "Jim")

Jim.deposit(100)

Sara.transfer(100, Jim)

Blaze = SavingsAcct(1000, 'Blaze')
Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(10000, Sara)
Blaze.transfer(1000, Sara)