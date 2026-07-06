"""
String69. Lotin harflari, ochuvchi “(” va yopuvchi “)” qavslardan iborat satr berilgan.
Agar qavslar to’g’ri qo’yilgan bo’lsa 0 chiqarilsin. Agar yopuvchi qavs noto’g’ri qo’yilgan
bo’lsa, uning o’rni (indeksi) chiqarilsin. Agar yopuvchi qavslar yetishmasa -1
chiqaruvchi programma tuzilsin.
"""

s = input("Satrni kiriting: ")
balans = 0

for i in range(len(s)):
    if s[i] == '(':
        balans += 1
    elif s[i] == ')':
        balans -= 1
        if balans < 0:
            print(i)
            break
else:
    if balans == 0:
        print(0)
    else:
        print(-1)
