"""
Minmax24. N natural soni va N ta butun sondan iborat to’plam berilgan (N > 1). Ikkita
qo’shni son yig’indisining eng katta qiymatni aniqlovchi programma tuzilsin. Massivdan
foydalanmang.
"""
# Nechta sonni qabul qilamiz shuni qabul qilamiz 
n = int(input())
# Boshlangich ikkita sonni olamiz va ularni max_sum yani (eng katta) son deb olamiz 
prev = int(input())
x = int(input())

max_sum = prev + x
# Bizga faqat siklmi ozi kerak i kerak emas biz boshlangich ikkita sonni qabul qilib 
# shunig uchun endi n-2 boladi sikkilar soni ikkiga kamayadi 
for _ in range(n - 2):
    # Sikl ichida eng muhim joyi hozirgi ikkinchi sonni yoqotib qoyomaslik kersak
    # Shunig uchun ikkinchini birinchi deb olamiz va qolgan sonlarni qabul qilib boshlaymiz
    prev = x
    x = int(input())
# Shart kiritamiz boshida kiritkan ikkinchi son bilan undan keyingi kelgan son yigindisi 
# boshidagi max_sum dan katta bolsa demak max_sum endi ozgaradi yani hozirgi qiymatni olaid 
    if prev + x > max_sum:
        max_sum = prev + x
# Va natijani chiqaradi endi albata max_sum ni oladi 
print(max_sum)

