"""
Matrix11. m x n o’lchamli matritsa berilgan. Matritsaning elementlarini spiral shaklida
chiqaruvchi programma tuzilsin. 0 – satr chapdan o’ngga, 1 – satr o’ngdan chapga, 2
– satr chapdan o’ngga, …
"""
m, n = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    if i % 2 == 0:
        print(*a[i])
    else:
        print(*a[i][::-1])

