"""
Dog klassini yarating.

Atributlari: name, age
Metodlari: Info() — itning ismi va yoshini chiqarsin.
           Bark() — "Vov-vov!" deb chiqarsin.
"""
class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def Info(self):
        print(self.name)
        print(self.age)
        
    def Bark(self):       
        print("Vov-vov")
        
dog1 = Dog("Reks", 5)
dog1.Info()
dog1.Bark()