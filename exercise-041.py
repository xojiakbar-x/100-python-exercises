"""
.Array113. n ta elementdan tashkil topgan massiv berilgan. Oddiy tanlash (selection
sort) algoritmi orqali massivni o’sish tartibida chiqaruvchi programma tuzilsin.
Algoritm quyidagicha: Har bir element o’zidan keyin turgan elementlarning eng kichigi
bilan almashtiriladi
"""
n = int(input())
a = list(map(int, input("n ta son kiriting ").split()))
a.sort()
print(a)         
