"""
FunSimple54. MonthDays funksiyasidan foydalangan xolda, PrevDate(D, M, Y)
funksiyasini hosil qiling. Funksiya berilgan sanadan oldingi sanani satr shaklida
qaytarsin. Berilgan sanadan oldingi sanani aniqlovchi dastur tuzilsin. (Oldingi
masalalarga qarang.)
"""
# FunSimple53 
def IsLeapYear(Year):
    return (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0)

def MonthDays(Month, Year):
    if Month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif Month in [4, 6, 9, 11]:
        return 30
    else:
        if IsLeapYear(Year):
            return 29
        else:
            return 28
# FunSimple53 
# Funksiyani yaratib olamiz unga 3 ta parametr beriladi  kun, oy, yil
def PrevDate(D, M, Y):
# Agar kun birdan katta bolsa shart juda ham oson kundan birni ayrib qoyamiz 
    if D > 1:
        D -= 1
# Agar kun birg teng bolgandagi shartlarni koramiz endi     
    else:
# Agar kun birg teng bolsa oy ham birga teng bolsa bir yol ortka qaytamiz oyimiz oz ozidan 12 oyga tenglashtiriladi 
        if M == 1:
            M = 12
            Y -= 1
# Aks holda oydan birni ayrib qoyish kifoya qiladi 
        else:
            M -= 1
# Shu joyda bitta masala bor agar hozir else shartida kun D=1 bolib turubdi oy M>1 dan bolib turibdi 
# Demak istalgan birdan katta oy olamiz masalan M=2 kun esa D=1 (D=1,M=2) bunday holatda 
# Bitta oldingi oyga o'tamiz muammo bu oy qaysi sana bilan tugashini bilmaymiz buni hal qilish uchun FunSimple53 
        D = MonthDays(M, Y) 
# Endi fu funksiya PrevDate nimani qaytarsin 
    return f"{D}/{M}/{Y}"

# kirish
D = int(input())
M = int(input())
Y = int(input())

print(PrevDate(D, M, Y))