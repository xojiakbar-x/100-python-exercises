"""
Ikkita butun son berilgan Day (kun) va Month (oy). (Kabisa bo`lmagan yil sanasi
kiritiladi). Berilgan sanadan keyingi sanani ifodalovchi programma tuzilsin

"""
# Daslab kun oyni qabul qilib olamiz  

kun = int(input("Kunni kiriting: "))
oy = int(input("Oyni kiriting:"))

# Kabisasiz yil oylari olinadi 
oy_kunlari = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Shart qoyamiz berilgan shartka kora 
if oy<1 or oy>12:
    print("Bunday oy yoq")
elif kun<1 or kun>oy_kunlari[oy-1]:
    print("Bunday kun yoq")
else:
    if kun == oy_kunlari[oy-1]:
        oy += 1
        kun = 1
    else:
        kun += 1
    if oy>12:
        oy = 1
    print(f"{kun:02}.{oy:02}")
