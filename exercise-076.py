"""
Recur9. Evklid algoritmi yordamida ikkita musbat A va B sonlarining eng katta umumiy
bo’luvchisini topuvchi (EKUB) butun toifadagi EKUB(A, B) rekursiv funksiyasi tuzilsin:
EKUB(A,B) = EKUB(B, A mod B), agar B 0; EKUB(A,0)=A.
Agar A,B sonlari berilgan bo’lsa, shu funksiya yordamida EKUB(A,B) topilsin
"""

def EKUB(A, B):
    if B == 0:
        return A
    return EKUB(B, A % B)

A = int(input("A = "))
B = int(input("B = "))
natija = EKUB(A, B)
print("EKUB =", natija)
