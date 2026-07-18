"""
Person nomli ota class yarating.

Unda:
name atributi bo'lsin.
Info() metodi ismni ekranga chiqarsin.
Walk() metodi "Yurmoqda." deb chiqarsin.

Student nomli bola class yarating.
Person classidan meros olsin.
Study() metodi "Dars qilmoqda." deb chiqarsin.

So'ng:
"Ali" nomli student yarating.
Info(), Walk(), Study() metodlarini chaqiring.
"""
class Person:
    def __init__(self, name):
        self.name = name
    
    def Info(self):
        print(self.name)
        
    def Walk(self):
        print("Yurmoqda.")

class Student(Person):
    def Study(self):
        print("Dars qilmoqda!")

talaba = Student("Ali")

talaba.Info()
talaba.Walk()
talaba.Study()        