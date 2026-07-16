"""
Phone klassi tuzilsin.
Maydonlari: brand — telefon markasi
            price — narxi
            memory — xotirasi (GB)
Metodlari:  Info() — telefon ma'lumotlarini chiqarsin.
            Discount() — narxning 10% chegirmadagi qiymatini chiqarsin.
"""
class Phone:
    def __init__(self, brand, price, memory):
        self.brand = brand
        self.price = price
        self.memory = memory
    def Info(self):
        return f"""Telefon markasi: 
    {self.brand}
    Narxi: {self.price}
    Xotirasi (GB): {self.memory}"""

    def Discount(self):
        return self.price * 0.9
    
phone1 = Phone("Android", 120, 100)
print(phone1.Info())
print(phone1.Discount())