"""
String68. Raqam va kichik lotin harflaridan iborat satr berilgan. Agar satrdagi harflar
alfavit tartibida bo’lsa 0 chiqaruchi, aks xolda qonuniyatni buzgan birinchi belgini
chiqaruvchi programma tuzilsin.
"""
s = input("Satrni kiriting: ")

oldingi = ""

for belgi in s:
    if belgi.isalpha():
        if oldingi != "" and belgi < oldingi:
            print(belgi)
            break
        oldingi = belgi
else:
    print(0)

