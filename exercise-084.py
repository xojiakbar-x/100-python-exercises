"""
Class4
Student klassi tuzilsin. 
Unda name va age maydonlari bo'lsin. 
Show() metodi talabaning ismi va yoshini ekranga chiqarsin. 
Berilgan ma'lumotlar uchun Show() metodi chaqirilsin.
"""
class Student:
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
    def show(self):
        print("Ismi:", self.name)
        print("Yoshi:", self.name)
        
        
student1 = Student("Ali", 20)
student1.show()  
        

