"""
FunSimple55. MonthDays funksiyasidan foydalangan xolda, NextDate(D, M, Y)
funksiyasini hosil qiling. Funksiya berilgan sanadan keying sanani aniqlasin, D – kun,
Y – yil, M – oyini qaytarsin. Berilgan sanadan keying sana aniqlansin. (Oldingi
masalaga qarang.)
"""
def KabisaYili(Year):
    return (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0)

def MonthDays(Month, Year):
    if Month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif Month in [4, 6, 9, 11]:
        return 30
    else:
        if KabisaYili(Year):
            return 29
        else:
            return 28

def NextDate(Dey, Month, Year):
    if Dey != MonthDays(Month, Year):
        Dey += 1
    else:
        if Month ==12:
            Year += 1
            Dey = 1
            Month = 1
        else:
            Month += 1
            Dey = 1
    return f"{Dey}/{Month}/{Year}"

Dey = int(input("Kun: "))
Month = int(input("Oy: "))
Year = int(input("Yil: "))

print(NextDate(Dey, Month, Year))