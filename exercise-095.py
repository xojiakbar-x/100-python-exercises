"""
Animal nomli ota class yarating.
Unda: Sound() metodi "Hayvon ovoz chiqaryapti." deb chiqarsin.

Dog nomli bola class yarating: Animal classidan meros olsin.
Sound() metodini qayta yozing (override qiling).
Endi "Vov-vov!" deb chiqarsin.

So'ng:
Dog obyektini yaratib Sound() metodini chaqiring.
"""
class Animal:
    def Sound(self):
        print("Hayvon ovoz chiqaryapti.")

class Dog(Animal):
    def Sound(self):
        print("Vov-vov")

dog1 = Dog()
dog1.Sound()      