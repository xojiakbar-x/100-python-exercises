"""
n va m natural sonlari berilgan. m bazada joylashgan testlar soni. m ta savoldan n
tasini tasodifiy tanlab oluvchi programma tuzilsin. Ya'ni a massivida shunday n ta son
bo'lsinki ular takrorlanmasin. a[ i ] <> a[ j] , i <> j bo'lsin. Bu yerda a[ i ] <= m. Maqsad
shuki bir savol nomeri 2 marta takrorlanmasin. a massiv elementlari ekranga
chiqarilsin.
Sodda qilib aytganda m ta sondan n tasini takrorlanmaydigan qilib tanlab beruvchi
dastur tuzilsin.
"""
import random
n = int(input())
m = int(input())
a = []
for _ in range(1, m+1):
    son = int(input())
    a.append(son)
x = random.sample(a, n)
print(x)





