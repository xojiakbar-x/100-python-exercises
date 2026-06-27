"""
Matrix32. m x n o’lchamli matritsa berilgan. Musbat va manfiy elementlari soni teng
bo’lgan (nol inobatga olinmaydi) birinchi uchragan satr nomerini aniqlovchi programma
tuzilsin. Agar bunday satr bo’lmasa, “Bunday satr yo’q” deb chiqarilsin.
"""
m, n = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    musbat = 0
    manfiy = 0

    for j in range(n):
        if a[i][j] > 0:
            musbat += 1
        elif a[i][j] < 0:
            manfiy += 1

    if musbat == manfiy:
        print(i)
        break
else:
    print("Bunday satr yo'q")