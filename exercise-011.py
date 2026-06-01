"""
N sonini M soniga bo'lgandagi qoldiqni va butun qismini bo'lish amallarini ( /, % )
ishlatmasdan topuvchi dastur tuzilsin
"""
# Hardoimgiday foydalanuvchidan ma'lumot qabul qilib olamiz
n=int(input("N sonni kiriting: "))
m=int(input("M sonni kiriting: "))
# Bolmastan qoldiq va butun sonni topish bu sonni ayrish orqali 
# boladi toki bu ayrilmay qoygunga qadar 
# eng kamida biri ikkinchisidan katte yoki ten bolsin 
butub_qism=0
while n>=m:
    n=n-m
    butub_qism+=1
# Chiqqan natijani ozgaruvchiga yuklaymiz
qoldiq=n
print(qoldiq, butub_qism) 







