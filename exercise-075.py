"""
Recur5. Fibonachi sonlari ketma-ketligidagining N-elementni hisoblovchi butun
toifadagi Fib2(N) rekursiv funksiya tuzilsin (N butun son):
F1=F2=1,
(N <= 20 ). Fib1 funksiyaga qaraganda rekursiv chaqirishlarni kamaytirish uchun
(Recur4 masalaga qarang) hisoblab bo’lingan Fibonachi sonlarini saqlovchi yordamchi
massivdan foydalanilsin va unga Fib2 funksiyasi bajarilganda murojaat qilinsin. Fib2
funksiyasi yordamida berilgan nomerdagi 3 ta Fibonachi soni va natijalarni olish uchun
Fib1 funksiyani rekursiv chaqirishlar soni chop qilinsin.
"""
count = 0
A = [0] * 21
A[1] = 1
A[2] = 1

def Fib2(n):
    global count
    count += 1

    if A[n] != 0:
        return A[n]

    A[n] = Fib2(n - 1) + Fib2(n - 2)
    return A[n]
for i in range(3):
    n = int(input("N = "))

    count = 0
    natija = Fib2(n)

    print("Fib =", natija)
    print("Rekursiv chaqirishlar soni =", count)

