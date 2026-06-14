"""
FunSimple52. Mantiqiy qiymat qaytaruvchi IsLeapYear(Year) funksiyasini hosil qiling.
Funksiya berilgan Year – yil kabisa yili bo’lsa true, aks holda false qiymat qaytarsin.
Berilgan 3 ta yildan nechtasi kabisaligini aniqlovchi dastur tuzing. (Kabisalik shartini
bilish uchun IF28 masalaga qarang.)
"""
def IsLeapYear(Year):
    if (Year % 4 == 0 and Year % 100 !=0) or Year % 400 ==0:
        return True
    else:
        return False

a = int(input("a"))
b = int(input("b"))
c = int(input("c"))

count = 0

if IsLeapYear(a):
    count+=1
if IsLeapYear(b):
    count+=1
if IsLeapYear(c):
    count+=1
print(count)

