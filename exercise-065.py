"""
Param1. N o’lchamli A massivni eng kichik elementini topuvchi butun toifadagi
MinElement(A, N) funksiyasi tuzilsin. Shu funksiya yordamida mos ravishda N
o’lchamdagi A massiv elementlarining eng kichikgi topilsin
"""

def MinElement(A, N):
    minimum = A[0]
    for i in range(1, N):
        if A[i] < minimum:
            minimum = A[i]
        return minimum