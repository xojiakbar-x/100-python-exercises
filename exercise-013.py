"""
Minmax4. N natural soni va n ta sonlar to’plami berilgan. Kiritilgan to’plamdagi eng
kichik element va uning o’rnini aniqlovchi programma tuzilsin. Massivdan
foydalanmang.
"""

n = int(input())

for i in range(1, n + 1):
    x = int(input())

    if i == 1:
        eng_kichik = x
        orni = 1
    elif x < eng_kichik:
        eng_kichik = x
        orni = i

print(eng_kichik, orni)
