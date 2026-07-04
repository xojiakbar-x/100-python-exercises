"""
String45. Probel bilan ajratilgan o’zbekcha so’zlardan iborat satr berilgan. Satrdagi
eng qisqa so’z uzunligini aniqlovchi programma tuzilsin.
"""
# Sozlarni kiritib olamiz 
s = input("Satrni kiriting: ")
# Kiritilgan sozlrni list korinichi keltirib olamiz 
words = s.split()
# Ichidan birinchi elementni eng kichik deb olamiz va qolganlarni shu bilan soishtiramiz
min_word = len(words[0])
# Sikl va shart kiritamiz 
for w in words:
    if len(w) < min_word:
        min_word = len(w)
print(min_word)       


