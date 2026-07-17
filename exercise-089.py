"""
BankAccount klassini yarating.
Atributlari: owner, balance
Metodlari: Info()
           Deposit(amount) — hisobga pul qo'shsin.
           Withdraw(amount) — pul yechsin.
Agar yechilayotgan pul balansdan ko'p bo'lsa: Hisobda mablag' yetarli emas.
aks holda pulni yechsin.
"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def Info(self):
        print("Hisob egasi: ", self.owner)
        print("Balans: ", self.balance)
    def Deposit(self, amount):
        self.balance += amount
        print(amount, "so'm hisobga qo'shildi.")
    def Withdraw(self, amount):
        if amount > self.balance:
            print("Hisobda pul yetarli emas!")
        else:
            self.balance -= amount
            print(amount, "so'm yechildi")


account = BankAccount("Ali", 500000)
account.Info()
account.Deposit(200000)
account.Withdraw(300000)
account.Withdraw(600000)
account.Info()        
        
        
        