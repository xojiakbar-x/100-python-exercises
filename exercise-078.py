"""
Recur11. Takrorlanish operatoridan foydalanmagan holda o’lchami N ga teng bo’lgan
A butun sonlar massivining eng katta elementini topuvchi MaxElem(A,N) funksiyasi
tuzilsin. Shu funksiya yordamida mos ravishda o’lchami N bo’lgan A massiv
elementlarining eng kattasi topilsin
"""

def MaxElem(A, N):
    if N == 1:
        return A[0]

    return max(A[N-1], MaxElem(A, N-1))


N = int(input())
A = list(map(int, input().split()))

print(MaxElem(A, N))




