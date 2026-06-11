"""
FunSimple46. Butun qiymat qaytaruvchi EKUB(A, B) funksiyasini hosil qiling.
Funksiya A va B sonlarining eng katta umumiy bo’luvchisini qaytarsin.
"""
# Funksiyani yaratib olamiz 
def EKUB(A, B):
# Biz EKUB ni topishda ecvivalent ususlidan foydalanmiz orin almshtirish bunga kora a b ga yoki b a ga bolinsin 
    while B!=0:
        A,B = B,A%B
    return A
# Foydalanuvchidan sonlarni qabul qilib olamiz va shu sonlarni ekub larin topamiz 
A = int(input("A sonni kiriting: "))
B = int(input("B sonni kiriting: "))
print(EKUB(A, B))






