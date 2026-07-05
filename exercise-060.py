"""
String59. Faylning to’liq nomini o’zida akslantirgan satr berilgan. Ya’ni disk nomi,
kataloglar nomi, faylning nomi va kengaytmasi. Satrdan faylning kengaytmasini
aniqlovchi programma tuzilsin.
"""
s = input()
oxiri = s.split("\\")[-1]
fayl = oxiri.split(".")[1]
print(fayl)