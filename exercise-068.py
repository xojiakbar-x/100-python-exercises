"""
Param10. N ta butun sondan iborat bo’lgan A massivning X soniga teng bo’lgan
elementini ikkilantiruvchi DoubleX(A, N, X) protsedurasi tuzilsin. A massiv va N kiruvchi
va chiquvchi parametrlar hisoblanadi. Shu protsedura yordamida mos ravishda
o’lchami N bo’lgan A massivning X sonlariga teng bo’lgan elementlari ikkilantirilsin va
hosil bo’lgan massiv va uning o’lchami chop qilinsin.
"""

def DoubleX(A, N, X):
    i = 0

    while i < N:
        if A[i] == X:
            A.insert(i + 1, X)
            N += 1
            i += 2   # yangi qo'shilgan elementni qayta tekshirmaslik uchun
        else:
            i += 1

    return N


# Asosiy dastur
N = int(input("N = "))
A = list(map(int, input("Massiv elementlari: ").split()))
X = int(input("X = "))

N = DoubleX(A, N, X)

print("Hosil bo'lgan massiv:")
print(*A)

print("Yangi o'lcham:")
print(N)       