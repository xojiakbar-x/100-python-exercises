"""
Recur4. Fibonachi sonlari ketma-ketligidagining N - elementni hisoblovchi butun
toifadagi Fib1(N) rekursiv funksiya tuzilsin (N butun son):
F1=F2=1,
Shu funksiya yordamida berilgan nomerdagi 3 ta Fibonachi soni va natijalarni olish
uchun Fib1 funksiyani rekursiv chaqirishlar soni chop qilinsin.
"""
count = 0

def Fib1(n):
    global count
    count += 1
    if n == 1 or n == 2:
        return 1
    return Fib1(n - 1) + Fib1(n - 2)
for i in range(3):
    n = int(input("N = "))

    count = 0
    javob = Fib1(n)

    print("Fib =", javob)
    print("Funksiya chaqirilgan soni =", count)

