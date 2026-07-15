"""
Class1
Inson - nomli class yarating.
Class quyidagi atributga ega bo'lsin: ism
Class quyidagi metodga ega bo'lsin: salom() — ekranga "Salom!" matnini chiqarsin.
So'ng Inson classidan bitta obyekt yarating va salom() metodini chaqiring.
"""
class Inson:

    def __init__(self, ism):
        self.ism = ism

    def salom(self):
        print("Salom!")

odam1 = Inson("Ali")

odam1.salom()

