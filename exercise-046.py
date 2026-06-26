"""
Matrix19. m x n o’lchamli matritsa berilgan. Matritsaning har bir satri elementlari
yig’indisini chiqaruvchi programma tuzilsin.
"""

m, n = map(int,input().split())
a = [list(map(int, input().split())) for _ in range(m)]
for i in range(m):
    print(sum(a[i]))
