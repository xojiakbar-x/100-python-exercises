"""
FunSimple53. IsLeapYear(Year) funksiyasidan foydalangan xolda, butun qiymat
qaytaruvchi MonthDays(Month, Year) funksiyasini hosil qiling. Funksiya berilgan Year
– yilning Month – oyi kunlar sonini qaytarsin. Berilgan yilning M1, M2, M3 oylarining
kunlar soni topilsin. (oldingi masalaga qarang.)
"""
def IsLeapYear(Yil):
    if (Yil % 4 == 0 and Yil % 100 != 0) or (Yil % 400 == 0):
        return True
    else:
        return False

def FunSimple53(Month, Year):
    if Month in [1, 3, 5, 7, 8, 10, 11]:
        return 31
    elif Month in [4, 6, 9, 11]:
        return 30
    elif Month == 2:
        if IsLeapYear(Year):
            return 29
        else:
            return 28

Year = int(input(" Yiklni kiriting: "))

M1 = int(input("Birinchi oyni kiriting: "))
M2 = int(input("Ikkinchi oyni kiriting: "))
M3 = int(input("Uchunchi oyni kiriting: "))


print(FunSimple53(M1, Year))
print(FunSimple53(M2, Year))
print(FunSimple53(M3, Year))
