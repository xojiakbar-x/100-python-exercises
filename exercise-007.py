"""
N natural soni berilgan. N gacha bo’lgan do’st sonlarni chiqaruvchi programma tuzilsin.
Agar birinchi son bo’luvchilari yig’indisi ikkinchi songa, ikkinchi son bo’luvchilari
yig’indisi birinchi songa teng bo’lsa, bu sonlar do’st sonlar deyiladi
"""
n=int(input("N natural sonni kiriting: "))
for a in range(2, n+1):
    yigindi_a=0
    # a sonni bo'luvchilari yigindisin topish
    for i in range(1, a):
        if a%i==0:
            yigindi_a+=i
    b=yigindi_a
    #  Do‘st sonlar bolish sharti shu shart bajarilganda keyingi shartka otadi  
    if b>a and b<=n:
        yigindi_b=0
    # b sonni boluchilarini yigindisini tekshiramiz 
        for i in range(1, b):
            if b%i==0:
                yigindi_b+=i
    # Sikl tugagach yigindi_b ni a ga tengligini tekshiramiz
        if yigindi_b==a:
            print(a, b)        
