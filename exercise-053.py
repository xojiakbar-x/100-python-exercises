"""
Matrix. Elementlari butun sonlardan iborat bo`lgan, mxn o`lchamli massiv berilgan.
Massivni eng kichik elementi turgan satrni olib tashlovchi programma tuzilsin.
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
satr = 0
# Shart kiritib eng kichik sonni tanlab olamiz
for i in range(m):
    for j in range(n):
        if a[i][j]<min:
            min = a[i][j]
            satr = i
a.pop(satr)
# Natijani chiqarish quydagicha 
for i in range(len(a)):
    print(*a[i])
    
            


