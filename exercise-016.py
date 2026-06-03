"""
Minmax11. N natural soni va N ta butun sondan iborat to’plam berilgan. Oxirgi
uchragan ekstremal element tartib raqamini aniqlovchi programma tuzilsin. Ekstremal
element deb eng katta yoki eng kichik elementga aytiladi. Massivdan foydalanmang.
"""
n = int(input())
x = int(input())

min_son = max_son = x
min_pos = max_pos = 1

for i in range(2, n + 1):
    x = int(input())

    if x < min_son:
        min_son = x
        min_pos = i

    if x > max_son:
        max_son = x
        max_pos = i

if min_pos < max_pos:
    print(min_son, min_pos)
    
else:
    print(max_son, max_pos)