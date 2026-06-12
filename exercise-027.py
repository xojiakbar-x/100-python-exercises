"""
FunSimple48. EKUB funksiyasidan foydalangan holda butun qiymat qaytaruvchi
EKUK(A, B) funksiyasini hosil qiling. Funksiya A va B sonlarining eng kichik umumiy
karralisini qaytarsin. EKUK = A * B / EKUB(A, B)
"""
# Bir dars oldingi funksiya 
def EKUB(A, B):
    while B != 0:
        A, B = B, A % B
    return A
# EKUK funksiyasi misolda ham keltirilgan faqat butun qismini olish uchun // dan foydalanmiz.
def EKUK(A, B):
    return A * B // EKUB(A, B)