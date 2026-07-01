"""
Matrix. Elementlari butun sonlardan iborat bo`lgan, mxn o`lchamli massiv berilgan.
Massivni eng kichik elementi turgan ustunni olib tashlovchi programma tuzilsin.
"""
# Daslab m va n sonlarni kiritib olamiz 
m = int(input("m sonni kiriting: "))
n = int(input("n sonni kiriting: "))
# Bo'sh list yartamiz keyingi kiritilgan matritsa elementlari shuni ichiga tushuadi 
a = []
# Elementlarni qabul qilamiz 
for i in range(m):
    qator = list(map(int, input("n ta son kiriting: ").split()))
    a.append(qator)
min = a[0][0]
ustun = 0
# Shart kiritib eng kichik sonni tanlab olamiz
for i in range(m):
    for j in range(n):
        if a[i][j]<min:
            min = a[i][j]
            ustun = j
for i in range(m):
    a[i].pop(ustun)
for i in range(m):
    print(*a[i])
    
            


