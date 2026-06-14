"""
N natural soni va N ta natural son berilgan. EKUB funksiyasidan foydalangan xolda
shu N ta sonning EKUBini aniqlovchi dastur tuzilsin. FunSimple46 ga qarang.
"""
# Birinchi EKUB funksiya yaratiladi 
def EKUBN(A,B):
    while B != 0:
        A, B = B, A % B
    return A
# N son qabul qilib olamiz 
N = int(input("N sonini kiritng: "))
# Har safar son kiritkanda bizda bitta son tayyor bolishi kerak shunig dastlabki sonni qabul qilib olamiz 
natija = int(input("A sonini kiritng: "))
for i in range(N-1):
    son = int(input(" sonni kiritng: "))
# Shu joyda bizda kiritlgan birinchi son foyda beradi har safar chiqqan natijani unga yuklab boramiz 
    natija = EKUBN(natija, son)
# Natijani print yordamida chiqaramiz
print(natija)
    