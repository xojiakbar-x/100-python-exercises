"""
Array17. n ta elementdan tashkil topgan massiv berilgan. Massiv elementlarini
quyidagicha chiqaruvchi programma tuzilsin. A[0], A[1], A[n-1], A[n-2], A[3], A[4], A[n-
3], A[n-4]
"""
n = int(input())
A = list(map(int, input().split()))

i = 0
j = n - 1

while i <= j:
    if i <= j:
        print(A[i], end=" ")
        i += 1

    if i <= j:
        print(A[i], end=" ")
        i += 1

    if i <= j:
        print(A[j], end=" ")
        j -= 1

    if i <= j:
        print(A[j], end=" ")
        j -= 1
