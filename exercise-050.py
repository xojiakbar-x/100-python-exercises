"""
Matrix. Elementlari butun sonlardan iborat bo`lgan, mxn o`lchamli massiv berilgan.
Har bir ustunning eng katta qiymatini m - satrga o`zlashtiruvchi programma tuzilsin.
"""
m = int(input("Satrlar soni: "))
n = int(input("Ustunlar soni: "))

a = []

for i in range(m):
    qator = list(map(int, input().split()))
    a.append(qator)

# Ustunlarning maksimumlarini saqlash uchun yangi ro'yxat
max_qator = []

for j in range(n):
    maxi = a[0][j]

    for i in range(1, m):
        if a[i][j] > maxi:
            maxi = a[i][j]

    max_qator.append(maxi)

# Yangi satr sifatida qo'shish
a.append(max_qator)

# Natijani chiqarish
for i in range(len(a)):
    print(*a[i])