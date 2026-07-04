"""
String40. Kamida bitta probeldan iborat satr berilgan. Satridagi birinchi va oxirgi probel
orasidagi belgilarni chiqaruvchi programma tuzilsin. Agar satr faqat bitta probeldan
iborat bo’lsa, bo’sh satr chiqarilsin.
"""
# Satrni qabul qilib olamiz
satr = input("Satrni kiriting: ")
# Satrni birinchi probelini topish string metodini ishlatamiz
birinchi = satr.find(" ")
# Oxirgi probelni topish metodini ishlatamiz
oxirgi = satr.rfind(" ")
# Shart qoyamiz 
if birinchi == oxirgi:
    print("Natija: ",end=" ")
    print("")
else:
    print(satr[birinchi+1 : oxirgi])