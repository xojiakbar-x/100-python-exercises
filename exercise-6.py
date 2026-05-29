"""
6.N natural soni berilgan. Shu songacha bo’lgan tub sonlarni
chiqaruvchi programma tuzilsin.
"""
# Daslab biror sonni qabul qilib olamiz.
n = int(input("Sonni kiriting: "))
print("Berilgan songacha bolgan tub sonlar.")
"""
Berilgan songacha bolgan barcha sonni tub deb olamiz 
keyingi shartda xatolarni tekschiramiz
"""
for son in range(2, n+1):
    tub=True
# Endi shart qoyamiz tub bolmaganlarni chiqarib tashlaymiz.
    for i in range(2, int(son**0.5)+1):
        if son%i==0:
            tub=False
            break
# Bu shartda biz endi tub sonlarni ekranga chiqaramiz.
    if tub:
        print(son, end=", ")