"""
Matrix. Elementlari butun sonlardan iborat bo`lgan, mxn o`lchamli massiv berilgan.
Har bir satrning eng katta qiymatini n - ustunga o`zlashtiruvchi programma tuzilsin.
"""

m, n = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    max_val = a[i][0]

    for j in range(n):
        if a[i][j] > max_val:
            max_val = a[i][j]

    # Eng katta elementni satr oxiriga qo'shish
    a[i].append(max_val)

# Natijani chiqarish
for i in range(m):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()
    

