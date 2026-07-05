"""
String61. Faylning to’liq nomini o’zida akslantirgan satr berilgan. Ya’ni disk nomi,
kataloglar nomi, faylning nomi va kengaytmasi. Satrdan oxirgi katalog nomini
aniqlovchi programma tuzilsin. Agar katalog tub bo’lsa (корневой), “\” belgisi
chiqarilsin.
"""
s = input()
birinchipapka = s.split("\\")[-2]
if s.split("\\")[1] == s.split("\\")[-1]:
    print("\\")
else:
    print(birinchipapka)
