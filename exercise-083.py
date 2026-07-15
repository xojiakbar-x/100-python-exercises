"""
Class3
Kitob nomli class yarating.
Class quyidagi atributga ega bo'lsin: nomi
Class quyidagi metodga ega bo'lsin: oqish() — ekranga "Kitob o'qilmoqda." matnini chiqarsin.
Bitta obyekt yarating va metodni chaqiring.
"""

class Kitob:
    def __init__(self, nomi):
        self.nomi = nomi
    
    def oqish(self):
        print("Kitob o'qilmoqda!")
        
Oq_Kema = Kitob("Oq_Kema")

Oq_Kema.oqish()
    


