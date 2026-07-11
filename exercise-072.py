"""
.Recur2. N!!=N*(N-2)*(N-4)*… ifodani hisoblovchi haqiqiy toifadagi Fact2(N) rekursiv
funksiyasi tuzilsin. (N>0 – butun toifadagi parameter; agar N juft son
bo’lsa, ko’paytmadagi oxirgi ko’paytuvchi 2 ga va agar N toq son bo’lsa, u holda 1
ga teng). Shu funksiya yordamida berilgan sonning ikkilangan faktoriali hisoblansin
"""
def Fact2(n):
    if n == 1 or n == 2:
        return n
    return n * Fact2(n - 2)

n = int(input("N = "))
print("N!! =", Fact2(n))

