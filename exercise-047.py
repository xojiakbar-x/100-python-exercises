"""
Matrix20. m x n o’lchamli matritsa berilgan. Matritsaning har bir ustuni elementlari
ko’paytmasini chiqaruvchi programma tuzilsin.
"""
# Daslab ikkita soni qabul qilib olamiz 
m, n = map(int, input().split())
# Matritsani hosil qilib olamiz 
a = [list(map(int, input().split())) for _ in range(m)]
# Shart qoyamiz 
for i in range(m):
    k = 1 
    for j in range(n):
        k *= a[i][j]
    print(k)
    
    