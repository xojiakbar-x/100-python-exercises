"""
While15. Bankka boshlang’ich Summa so’mda qo’yildi. Har oyda bor bo’lgan summa p
foizga oshadi (0 < p < 12 ). Necha oydan keyin boshlang’ich qiymat 2 martadan ko’p
bo’lishini hisoblovchi programma tuzilsin. Necha oy k – butun son. Bankda hosil
bo’lgan summa haqiqiy son ekranga chiqarilsin.
"""
# Daslab summa va foizni qabul qilib olamiz 
summa = float(input("Boshlang'ich summani kiriting: "))
p = float(input("Foizni kiriting: "))
# Boshlangich summani biror ozgaruvchiga qabul qilb olamiz bu bizga while siklida kerak boladi 
boshlangich = summa
k = 0
# while sikliga shart kiritamiz berilgan masala boyicha 
while summa <= 2 * boshlangich:
    summa += summa * p / 100
    k += 1
# Shart bajarilmasa natijani chiqaradi 
print("Oylar soni:", k)
print("Hosil bo'lgan summa:", summa)
