"""
Minmax1. N natural soni va n ta sonlar to’plami berilgan. Kiritilgan to’plamdagi eng
katta va eng kichik sonni topuvchi programma tuzilsin. Massivdan foydalanmang.
"""
n = int(input("N ni kiriting: "))

son = float(input("1-sonni kiriting: "))
eng_kichik = son
eng_katta = son

for i in range(2, n + 1):
    son = float(input(f"{i}-sonni kiriting: "))

    if son < eng_kichik:
        eng_kichik = son

    if son > eng_katta:
        eng_katta = son

print("Eng kichik son:", eng_kichik)
print("Eng katta son:", eng_katta)