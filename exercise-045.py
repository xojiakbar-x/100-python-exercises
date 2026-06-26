"""
Matrix13. MxM o'lchamli kvadrat matritsa A berilgan. A0,0 elementdan boshlab
martitsa elementlari quyidagicha chiqarilsin (burchak hosil qilgan holda): birinchi
satrning barcha elementlari; oxirgi ustunning barcha elementlari (birinchi elementidan
tashqari, chunki u chiqarilgan); ikkinchi satrning qolgan elementlari; oxirdan bir oldingi
ustunning qolgan elementlari; va xakazo; oxirda AM-1,0 element chiqadi
"""
m = int(input())

a = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    print(*a[i][i:], end=" ")

    for j in range(i + 1, m):
        print(a[j][m - i - 1], end=" ")



