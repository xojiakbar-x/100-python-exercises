"""
String59. Faylning to’liq nomini o’zida akslantirgan satr berilgan. Ya’ni disk nomi,
kataloglar nomi, faylning nomi va kengaytmasi. Satrdan faylning kengaytmasini
aniqlovchi programma tuzilsin.
"""
s = input()
birinchipapka = s.split("\\")[1]
if s.split("\\")[1] == s.split("\\")[-1]:
    print("\\")
else:
    print(birinchipapka)
