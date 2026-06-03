"""
Minmax6. N natural soni va N ta butun sondan iborat to’plam berilgan. Birinchi
uchragan eng kichik va oxirgi uchragan eng katta element va ularning tartib raqamini
aniqlovchi programma tuzilsin. Massivdan foydalanmang.
"""

n = int(input("N ni kiriting: "))  # nechta son kirishini olamiz

for i in range(1, n + 1):
    x = int(input()) 

    if i == 1:
        # birinchi sonni boshlang‘ich deb olamiz
        min_val = x
        max_val = x

        # pozitsiya (tartib raqami)
        min_pos = 1
        max_pos = 1

    else:
        # eng kichikni topish
        if x < min_val:
            min_val = x
            min_pos = i  

        # eng kattani topish
        if x > max_val:
            max_val = x
            max_pos = i  
         # katta sonni birinchisini emas oxirgisini olish   
        elif x == max_val:
            max_pos = i  

print(min_val, min_pos)
print(max_val, max_pos)