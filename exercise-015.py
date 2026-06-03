"""
Minmax10. N natural soni va N ta butun sondan iborat to’plam berilgan. Birinchi
uchragan ekstremal element va uning tartib raqamini aniqlovchi programma tuzilsin.
Ekstremal element deb eng katta yoki eng kichik elementga aytiladi. Massivdan
foydalanmang.
"""
# sonni qabul qilib olamiz foydalanuvchidan 
n=int(input("N sonni kiriting: "))
x=int(input())
# Birinchi son enga katta ham bolishi mumkun eng kichigi ham bolishi mumkun
son_min=son_max=x
min_pas=max_pas=1
# for shartini kiritamiz qolgan sonlarni qabul qilish uchun 
for i in range(2,n+1):
    x=int(input())
    # eng kichik sonni tanlab olamiz if sharti orqali 
    if x<son_min:
        son_min=x
        min_pas=i
    # eng katta sonni tanlab olamiz if sharti orqali 
    if x>son_max:
        son_max=x
        max_pas=i
    # va albatta berlgan shart asosida birinchi uchragan eng katta yoki eng kichik sonni olamiz 
if min_pas<max_pas:
    print(son_min, min_pas)
else:
    print(son_max,max_pas)

