"""
Param21. O’lchami MxN ga teng, elementlari haqiqiy sonlardan iborat bo’lgan A
matritsaning K-satrda joylashgan elementlarining yig’indisini hisoblovchi SumRow(A,
K) funksiyasi tuzilsin. Agar K>M bo’lsa, u holda funksiya 0 qiymat qaytaradi. Berilgan
K soni va A matritsa uchun SumRow(A,K) topilsin.
"""

def SumRow(A, K):
    M = len(A)

    if K > M:
        return 0

    summa = 0

    for x in A[K-1]:
        summa += x

    return summa





