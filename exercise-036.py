"""
Array40. n ta elementdan tashkil topgan massiv va R butun soni berilgan. Massiv
elementlari orasidan R soniga eng yaqin sonni topuvchi programma tuzilsin. Agar
bunday sonlar bir nechta bo'lsa, birinchisi chiqarilsin.
( |a[k] - R| ayirma eng kichik bo’luvchi a[k] topilsin )
"""
n = int(input())
A = list(map(int, input().split()))
R = int(input())

eng_yaqin = A[0]
min_farq = abs(A[0] - R)

for i in range(1, n):
    farq = abs(A[i] - R)

    if farq < min_farq:
        min_farq = farq
        eng_yaqin = A[i]

print(eng_yaqin)