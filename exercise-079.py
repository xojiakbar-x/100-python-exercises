"""
Recur12. Takrorlanish operatoridan foydalanmagan holda S satrdagi raqamlar sonini
aniqlovchi butun toifadagi DigitCount(S) rekursiv funksiyasi tuzilsin. Shu funksiya
yordamida berilgan satrdagi raqamlar soni aniqlansin.
"""

def DigitCount(S):
    if len(S) == 0:
        return 0
    if S[-1].isdigit():
        return 1 + DigitCount(S[:-1])
    else:
        return DigitCount(S[:-1])

S = input("Satrni kiriting: ")
print(DigitCount(S))
 


