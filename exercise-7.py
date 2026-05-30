n=int(input("N natural sonni kiriting: "))
for a in range(2, n+1):
    yigindi_a=0
    for i in range(1, a):
        if a%i==0:
            yigindi_a+=i
    b=yigindi_a
    if b>a and b<=n:
        yigindi_b=0
        for i in range(1, b):
            if b%i==0:
                yigindi_b+=i
        if yigindi_b==a:
            print(a, b)        