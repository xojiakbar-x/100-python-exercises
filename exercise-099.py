"""
1-masala

Student nomli klass yarating.

Unda:

name atributi bo'lsin.
__grade atributi private (yashirin) bo'lsin.

Quyidagi metodlarni yarating:

SetGrade(grade) — bahoni o'zgartirsin.
GetGrade() — bahoni ekranga chiqarsin.

So'ng:
"Ali" ismli student yarating.
Bahosini 90 qilib o'rnating.
Bahosini ekranga chiqaring.
"""
class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0

    def SetGrade(self, grade):
        self.__grade = grade

    def GetGrade(self):
        print("Baho:", self.__grade)


s1 = Student("Ali")

s1.SetGrade(90)
s1.GetGrade()