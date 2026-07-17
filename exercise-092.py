"""
Bir nechta abyekt bilan ishlash:
Color klassini yarating.
Atributi: name (rang nomi)
Metodi: Info() — rang nomini chiqarsin.
Bir nechta rang obyektlari yarating.
"""

class Color:
    def __init__(self, name):
        self.name = name

    def Info(self):
        print("Rang:", self.name)


rang1 = Color("Qizil")
rang2 = Color("Yashil")
rang3 = Color("Ko'k")


rang1.Info()
rang2.Info()
rang3.Info()

       