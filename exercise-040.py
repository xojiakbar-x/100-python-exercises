"""
Array112. n ta elementdan tashkil topgan massiv berilgan. Oddiy o’rin almashtirish
(pufaksimon saralash) algoritmi orqali massivni o’sish tartibida chiqaruvchi programma
tuzilsin.
Algoritm quyidagicha: Har bir element o’zidan keyin turgan elementlar bilan
solishtiriladi. Agar o’zidan keyin turgan element undan kichik bo’lsa ularni qiymati
almashtiriladi.
"""
n = int(input())
a = []
for _ in range(n):
    son = int(input())
    a.append(son)
a.sort()
print(a)


