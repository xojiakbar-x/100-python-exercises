"""
Minmax12. N natural soni va N ta butun sondan iborat to’plam berilgan. Eng kichik
musbat sonni aniqlovchi programma tuzilsin. Agar musbat son bo’lmasa nol
chiqarilsin. Massivdan foydalanmang.
"""
# Birinchi N natural son qabul qilamiz
n = int(input())
# Agar sonlar toplami manfiy bolsa 0 chiqaramizi 
eng_kichik_son=0
# Sikl tayorlaymiz n marotaba 
for i in range(n):
    x = int(input())
    if x > 0:
        if eng_kichik_son == 0 or x < eng_kichik_son:
            eng_kichik_son = x
print(eng_kichik_son)            