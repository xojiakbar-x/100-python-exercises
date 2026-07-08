"""
Param8. N ta butun sondan iborat bo’lgan A massivning X butun soniga teng bo’lgan
elementlarini o’chiruvchi RemoveX(A, N, X) protsedurasi tuzilsin. A va N kiruvchi va
chiquvchi parametrlar hisoblanadi. Shu protsedura yordamida o’lchami N ga teng
bo’lgan A massivning X elementi o’chirilsin. RemoveX ga har gal murojaat qilgandan
keyin, hosil bo’lgan massiv va uning o’lchami chop qilinsin. N <= 100
"""
def RemoveX(A, N, X):
    i = 0

    while i < N:
        if A[i] == X:
            A.pop(i)
            N -= 1
        else:
            i += 1

    return N


A = list(map(int, input("Massiv: ").split()))
N = len(A)

X = int(input("X = "))

N = RemoveX(A, N, X)

print("Yangi massiv:", A)
print("Yangi o'lcham:", N)