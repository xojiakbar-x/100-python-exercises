"""
Array35. n ta elementdan tashkil topgan massiv berilgan. Massiv lokal maksimumlari
orasidan kichigini chiqaruvchi programma tuzilsin. Lokal maksimum – o’ng va chap
qo’shinisidan katta bo’lgan element.
"""
n = int(input())
A = list(map(int, input().split()))

i = 1
mn = None

while i < n - 1:
    if A[i] > A[i - 1] and A[i] > A[i + 1]:
        if mn is None or A[i] < mn:
            mn = A[i]

    i += 1

print(mn)