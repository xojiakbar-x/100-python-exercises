"""
A va B natural sonlari berilgan. Evklid algoritmi bo'yicha EKUB(a,b) ni aniqlovchi dastur
tuzilsin. EKUB - Eng Katta Umumiy Bo`luvchisi.
"""
a = int(input("A ni kiriting: "))
b = int(input("B ni kiriting: "))
# Evklid algaritmi boyicha shart kiritamiz
while b != 0:
    qoldiq = a % b
    a = b
    b = qoldiq

print("EKUB =", a)

