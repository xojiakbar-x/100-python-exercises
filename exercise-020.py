"""
Minmax22. N natural soni va N ta butun sondan iborat to’plam berilgan (N > 2).
To’plamdagi eng kichik 2 ta qiymatni aniqlovchi programma tuzilsin. Massivdan
foydalanmang. Bu masalada xil son kiritilmaydi.
"""
n = int(input())
a = int(input())
b = int(input())

if a < b:
    min1, min2 = a, b
else:
    min1, min2 = b, a
for _ in range(n-2):
    x = int(input())
    if x < min1:
        min2 = min1
        min1 = x
    elif x < min2:
        min2 = x
print(min1, min2)
        


