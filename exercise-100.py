"""
BankAccount nomli klass yarating.

Unda:
owner atributi bo'lsin.
__balance atributi private (yashirin) bo'lsin.

Quyidagi metodlarni yarating:
Deposit(amount) — hisobga pul qo'shsin.
Withdraw(amount) — hisobdan pul yechsin.
GetBalance() — balansni ko'rsatsin.

Shart:
Agar yechilayotgan pul balansdan ko'p bo'lsa:
Hisobda mablag' yetarli emas chiqsin.
"""
class BankAccount:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        
    def Deposit(self, amount):
        self.__balance += amount
        
    def Withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Hisobda pul yetarli emas!")
            
    def GetBalance(self):
        print(self.__balance)

account = BankAccount("Ali", 1000)

account.Deposit(200)
account.Withdraw(300)
account.GetBalance()