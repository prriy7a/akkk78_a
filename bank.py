#create a bank account class having 2 attributes: Account holder name and balance
#and two methods: Deposit and withdraw
#Make some deposit and withdraw operation but withdraw amount cant exceed the available balance
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited {amount} to your account")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Not enough balance")
        else:
            self.balance-=amount
            print(f"Withdraw amount:{amount} from your account")
    def __str__(self):
        return f"Accountholder name:{self.name}\n Balance:{self.balance}"
user=BankAccount("Akshith",10000)
user.deposit(1000)
user.withdraw(100)
print(user)