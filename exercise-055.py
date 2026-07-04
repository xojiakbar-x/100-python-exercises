"""
String41. Probel bilan ajratilgan o’zbekcha so’zlardan iborat satr berilgan. Satrdagi
so’zlar sonini aniqlovchi programma tuzilsin
"""

# Satrni qabul qilib olamiz
s = input("Satrni kiriting: ")
# Satrdagi barcha bosh joylar sonini tpamiz string metodi count()
soni = s.count(" ")
# Mantiqqa ko'ra 2ta so'zda bitta probel 3 ta so'zda 2ta probel bo'ladi... . Probel so'zdan hamisha 1 taga kam boladi 
print(soni+1)



