"""
Class2
Mushuk nomli class yarating.
Class quyidagi atributga ega bo'lsin: nomi
Class quyidagi metodga ega bo'lsin: miyov() — ekranga "Miyov!" matnini chiqarsin.
Bitta obyekt yarating va metodni chaqiring.
"""
class Mushuk:
    def __init__(self, nomi):
        self.nomi = nomi
    
    def miyov(self):
        print("Miyov!")

qora_mushuk = Mushuk("qora_mushuk")
qora_mushuk.miyov()
