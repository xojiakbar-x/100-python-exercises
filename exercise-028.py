"""
FunSimple49. EKUB funksiyasidan foydalangan holda (oldingi masalalarga qarang)
butun qiymat qaytaruvchi EKUB3(A, B, C) funksiyasini hosil qiling. EKUB3 funksiyasi
3 ta sonning EKUBini aniqlaydi.
"""
def EKUB(A,B):
    while B != 0:
        A, B = B, A % B 
    return A
def EKUB3(A, B, C):
    return EKUB(EKUB(A,B),C)
    