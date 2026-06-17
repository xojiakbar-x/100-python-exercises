"""
Array16. n ta elementdan tashkil topgan massiv berilgan. Massiv elementlarini
quyidagicha chiqaruvchi programma tuzilsin. A[0], A[n-1], A[1], A[n-2], A[2], A[n-3],…
"""
n = int(input())
A = list(map(int, input().split()))

for i in range((n + 1) // 2):
    print(A[i], end=" ")

    if i != n - 1 - i:
        print(A[n - 1 - i], end=" ")
        
        



