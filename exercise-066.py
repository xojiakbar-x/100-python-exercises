"""
Param4. Elementlari haqiqiy sonlardan iborat bo’lgan N o’lchamli A massiv elemetlari
teskarisiga tartiblovchi Invert(A, N) protsedura tuzilsin. A massivi ham kiruvchi ham
chiquvchi parametr hisoblanadi. Shu protsedura yordamida mos ravishda o’lchamlari
N bo’lgan, A massiv invertlansin.
"""

def Invert(A, N):
    for i in range(N // 2):
        A[i], A[N - 1 - i] = A[N - 1 - i], A[i]
N = int(input("N = "))
A = []
for i in range(N):
    A.append(float(input()))
Invert(A, N)
print(A)
