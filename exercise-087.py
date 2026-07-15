"""
Class7
Product klassi tuzilsin. Unda quyidagi maydonlar bo'lsin:
* name — mahsulot nomi
* price — mahsulot narxi
* count — mahsulot soni
Total() metodi mahsulotlarning umumiy narxini hisoblasin.
Info() metodi mahsulot nomi, narxi va sonini ekranga chiqarsin.
Berilgan ma'lumotlar uchun Info() va Total() metodlari chaqirilsin.
"""

class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def Total(self):
        return self.price * self.count

    def Info(self):
        print("Mahsulot nomi:", self.name)
        print("Narxi:", self.price)
        print("Soni:", self.count)


product1 = Product("Olma", 5000, 10)

product1.Info()

print("Umumiy narx:", product1.Total())
    


