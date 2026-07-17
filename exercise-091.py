"""
Phone klassini yarating.
Atributlari: brand, price
Metodlari: Info(),Call() — "Qo'ng'iroq qilinmoqda." deb chiqarsin.
"""
class Phone:
    
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        
    def Info(self):
        print(self.brand)
        print(self.price)
        
    def Call(self):
        print("Qo'ng'iroq qilinmoqda")
        
phone1 = Phone("Iphone", 1200)

phone1.Info()
phone1.Call()
