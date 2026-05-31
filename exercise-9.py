"""
While19. n butun soni berilgan (n > 0). Bo’lib butun va qoldiq qismlarini aniqlash orqali,
berilgan son raqamlari sonini va raqamlari yig’indisini chiqaruvchi programma tuzilsin
"""

n = int(input("N son kiriting: "))

sonlar_soni = 0
yigindi = 0

while n > 0:
    yigindi += n % 10     # oxirgi raqam
    n = n // 10           # oxirgi raqamni olib tashlaymiz
    sonlar_soni += 1      # raqamlar sonini oshiramiz

print("Raqamlar soni:", sonlar_soni)
print("Raqamlar yig'indisi:", yigindi)