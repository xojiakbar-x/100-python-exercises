"""
String52. Probel bilan ajratilgan o’zbekcha so’zlardan iborat satr berilgan. Satrdagi
har bir so’zning birinchi harfini kattasi bilan almashtiruvchi programma tuzilsin. So’z
deganda probel, satr boshi yoki satr oxiri bilan ajratilgan belgilar ketma – ketligi
tushuniladi.
"""
s = input("Satrni kiriting: ")

sozlar = s.split()

for i in range(len(sozlar)):
    sozlar[i] = sozlar[i].capitalize()

natija = " ".join(sozlar)

print("Natija:", natija)