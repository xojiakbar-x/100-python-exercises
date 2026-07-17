"""
Animal nomli ota class yarating.
Unda:
name atributi bo'lsin.
Info() metodi hayvon nomini ekranga chiqarsin.
Sound() metodi "Ovoz chiqaryapti" matnini chiqarsin.

Dog nomli bola class yarating.

Dog classi Animal classidan meros olsin.
Unda Bark() metodi bo'lsin va "Vov-vov!" matnini chiqarsin.

So'ng:
"Bobik" nomli it obyektini yarating.
Obyekt orqali Info(), Sound(), Bark() metodlarini chaqiring.
"""
class Animal:
    def __init__(self, name):
        self.name = name 
        
    def Info(self):
        print("Nomi",self.name)
    
    def Sound(self):
        print("Ovoz chiqaryapti")   
class Dog(Animal):
    def Bark(self):
        print("Vov-vov")
Bobik = Dog("Bobik")

Bobik.Info()
Bobik.Sound()
Bobik.Bark()
         
        