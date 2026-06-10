"""
23.FunSimple29. Butun qiymat qaytaruvchi DigitCount(K) funksiyasini hosil qiling. (K >
0). Funksiya K ning raqamlari sonini qaytarsin
"""
def DigitCount(K):
    count = 0
    while K > 0:
        # 10 ga bolanda sonlar oxiridan bitta raqamga kamayib boradi bu siklda amalga oshirilsa 
        # sonni nechta raqamdan tashkil topkanligini bilish mumkun 
        K = K // 10
        count += 1
    return count
K = int(input("Son kiriting: "))
print("Raqamlar soni:", DigitCount(K))

