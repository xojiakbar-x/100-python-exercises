"""
Array114. n ta elementdan tashkil topgan massiv berilgan. Oddiy qo’shish (insertion
sort) algoritmi orqali massivni o’sish tartibida chiqaruvchi programma tuzilsin.
Algoritm quyidagicha: a[0]va a[1] elementlar o’sish tartibida joylashtiriladi. Ya’ni zarurat
bo’lsa qiymatlari almashtiriladi. Kiyin a[2] element saralangan elementlar (a[0], a[1])
orasiga shunday joylashtiriladiki, natijada a[0], a[1], a[2] tartiblangan xolatda bo’ladi.
Shu tartibda har bir element tartiblangan elementlar orasiga qo’shib boriladi.
"""
# 1-amal yordamida 
n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    key = a[i]
    j = i - 1

    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1

    a[j + 1] = key

print(a)

# 2-tayor metod funksiyalr yordamida 


