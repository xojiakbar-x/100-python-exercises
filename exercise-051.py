"""
Matrix. Elementlari butun sonlardan iborat bo`lgan, mxn o`lchamli massiv berilgan.
Massivni eng kichik elementining indeksini chiqaruvchi programma tuzilsin.
"""
# m va n sonlarni kiritib olamiz 
m = int(input("m butun son kiriting: "))
n = int(input("n butun son kiriting: "))
# a matritsa yaratib olamiz
a = []
for i in range(m):
    qator = list(map(int, input().split()))
    a.append(qator)
# Eng kichigini 0-satr 0-ustun deb olamiz keyingi kelgan sonlarni shu bilan solishtriamiz 
min = a[0][0]
satr = 0
ustun = 0

for i in range(m):
    for j in range(n):
        if a[i][j] < min:
            min = a[i][j]
            satr = i
            ustun = j
print(satr, ustun)

            
