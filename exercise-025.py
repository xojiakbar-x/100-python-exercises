"""
FunSimple31. IsPalindrom(N) mantiqiy funksiyasini hosil qiling. (N > 0). Agar N soni
palindrom bo’lsa – true, aks holda false qiymat qaytarilsin. O'ngdan chapga va
chapdan o'ngga bir xil o'qiladigan sonlar palindrom sonlar deyiladi. Shu funksiya orqali
3 ta sondan nechtasi palindrom ekanini aniqlovchi programma tuzilsin. IsPalindrom
funksiyasinida DigitCount va DigitN funksiyalridan foydalanish mumkin. (oldingi ikkita
masalaga qarang)
"""
# IsPalindrom(N) nomli funksiyani yaratib olamiz
def IsPalindrom(N):
# N>0 dan va N sonini teskarisi oziga teng bolganda True bolsin qolgan holatlarda False
    return N > 0 and N == int(str(N)[::-1])
# Kiritilgan sonni nechta raqamdan iborat ekanlini bilish uchun ozgaruvchi kerak 
count = 0
# Biz faqat 3 ta son kiritamiz 
for i in range(3):
    n = int(input("Son kiriting: "))
# Funksiyadan foydalanamiz True bolsa countga 1 qoshiladi
    if IsPalindrom(n):
        count += 1
# Natijani chiqaramiz 
print("Palindrom sonlar soni:", count)




