"""
Minmax13. N natural soni va N ta butun sondan iborat to’plam berilgan. Birinchi
uchragan eng katta toq element va uning tartib raqamini aniqlovchi programma tuzilsin.
Agar toq son bo’lmasa nol chiqarilsin. Massivdan foydalanmang.
"""
# Birinchi foydalanuchidan N sonini qabul qilib olamiz 
n = int(input("N natural son kiriting: "))
eng_katta_toq = 0
tartib = 0
# n ta son oladigan sikl yaratamiz
for i in range(1,n+1):
    x = int(input())
    if x % 2 != 0:
        if tartib == 0 or x > eng_katta_toq:
            eng_katta_toq=x
            tartib=i
if tartib == 0:
    print(0)
else:
    print(eng_katta_toq, tartib)
    