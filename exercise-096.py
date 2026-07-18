"""
Animal nomli ota class yarating.

Unda:
Sound() metodi "Hayvon ovoz chiqaryapti." deb chiqarsin.

Quyidagi bola classlarni yarating:
Dog → Sound() → "Vov-vov!"
Cat → Sound() → "Miyov!"

So'ng:
Dog va Cat obyektlarini bitta ro'yxatga joylang.

for sikli orqali har bir obyektning Sound() metodini chaqiring.
"""
class Animal:
    def Sound(self):
        print("Hayvon avoz chiqaryapti.")

class Dog(Animal):
    def Sound(self):
        print("Vov-vov")
        
class Cat(Animal):
    def Sound(self):
        print("Miyov")
        
dog = Dog()
cat = Cat()
    
animals = [dog, cat]

for animal in animals:
    animal.Sound()
    