"""
Param22. O’lchami MxN ga teng, elementlari haqiqiy sonlardan iborat bo’lgan A
matritsaning K – ustunda joylashgan elementlarining yig’indisini
hisoblovchi SumColumn(A, K) funksiyasi tuzilsin. Agar K>N bo’lsa, u holda funksiya
0 qiymat qaytaradi. Berilgan K soni va A matritsa uchun SumColumn(A,M,N,K)
topilsin.
"""

def SumColumn(A, K):
    M = len(A)
    N = len(A[0])
    
    if K > N:
        return 0
    
    summ = 0
    
    for i in range(M):
        summ += A[i][K-1]
        
    return summ

M, N = map(int, input("2 ta son kiriting: ").split())

A = []

for i in range(M):
    qator = list(map(int, input("N ta son kiriting: ").split()))
    A.append(qator)
    
K = int(input("K sonni kiriting: "))

print(SumColumn(A, K))






