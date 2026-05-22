"""
Yil berilgan (musbat butun son). Berilgan yilda nechta kun borligini aniqlovchi
programma tuzilsin. Kabisa yilida 366 kun bor, kabisa bo’lmagan yilda 365 kun bor.
Kabisa yil deb 4 ga karrali yillarga aytiladi. Lekin 100 ga karrali yillar ichida faqat 400
ga karrali bo’lganlari kabisa yil hisoblanadi. Masalan 300, 1300 va 1900 kabisa yili
emas. 1200 va 2000 kabisa yili.
""" 
yil = int(input("Yilni kiriting(x): "))
if (yil % 4 == 0 and yil % 100 !=0) or yil % 400 == 0:
    print(366)
else:
    print(365)
    