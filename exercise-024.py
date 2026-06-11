"""
FunSimple30. Butun qiymat qaytaruvchi DigitN(K, N) funksiyasini hosil qiling. (K > 0).
Funksiya K sonining N – raqamini qaytarsin. Agar K soni raqamlari N dan kichk bo’lsa,
minus bir qaytarilsin.
"""
# Daslab " DigitN " funksiyani yaratib olamiz 
def DigitN(K, N):
# K sonini string korinishiga otkazib olamiz 
    s = str(K)
# Agar K soni raqamlari N dan kichk bo’lsa, minus bir qaytarilsin.
    if N>len(s):
        return -1
# Shartdan keyin yana qiymat qaytarsin K sonini N - qiymatini 
    return int(s[N-1])
# Foydalanuvchidan K va N sonlarini qabul qilib olamiz 
K = int(input("K sonini kirting: "))
N = int(input("N sonini kiriting: "))
# Natijani chiqaramiz 
print(DigitN(K, N))








