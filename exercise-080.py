"""
Recur13. Agar S satr polindrom bo’lsa (ya’ni o’ngdan ham, chapdan ham bir xil
o’qiladigan) bo’lsa TRUE, aks holda FALSE qiymatini qaytaruvchi Polindrom(S)
rekursiv funksiyasi tuzilsin. Funksiya tanasida takrorlash operatoridan foydalanilmasin.
Berilgan satr uchun Polindrom funksiyasi qiymatlari chop qilinsin.
"""
def Polindrom(S):
    A = S[::-1]
    if A == S:
        return True
    else:
        return False
        
S = input("Satrni kiriting: ")
print(Polindrom(S))

