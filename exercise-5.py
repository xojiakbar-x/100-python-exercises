"""natural soni berilgan. Shu songacha bo’lgan mukammal sonlarni chiqaruvchi
programma tuzilsin. O`zidan boshqa bo’luvchilari yig’indisi o’ziga teng bo’lgan son
mukammal son deyiladi. Masalan: 6, 28"""

n=int(input("Sonni kiriting: "))

for son in range(1, n+1):
    yigindi = 0
    # Sonni bo'luvchilarini topish 
    for i in range(1, son):
        if son % i ==0:
            yigindi+=i
    # Sonni bo'luvchilarini tekshirish 
    if yigindi==son:
        print(son)
        