"""
FunSimple28. IsPrime(N) mantiqiy funksiyasini hosil qiling. (N > 0). Agar N soni tub
bo’lsa – true, aks holda false qiymat qaytarilsin. Shu funksiya orqali kiritilgan k ta
sondan nechtasi tub ekanini aniqlovchi programma tuzilsin.
"""
def IsPrime(N):
    if N < 2:
        return False

    for i in range(2, N):
        if N % i == 0:
            return False

    return True


k = int(input("k ni kiriting: "))

count = 0

for _ in range(k):
    n = int(input("son kiriting: "))
    if IsPrime(n):
        count += 1

print("Tub sonlar soni:", count)