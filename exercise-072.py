"""
Recur1. N!=1*2*…*N faktorialni hisoblovchi haqiqiy toifadagi Fact(N) rekursiv
funksiyasi tuzilsin. (N > 0 – butun toifadagi parameter ). Shu funksiya yordamida
berilgan sonning faktoriallari hisoblansin.
"""
def Fact(n):
    if n == 1:
        return 1
    return n * Fact(n - 1)


