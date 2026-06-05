"""
Minmax17. N natural soni va N ta butun sondan iborat to’plam berilgan. Oxirgi
uchragan eng katta elementni va keyin turgan elementlar sonini aniqlovchi programma
tuzilsin. Massivdan foydalanmang.
"""
# N sonini ozini qabul qilib olamiz dastlab
n = int(input())
# Bizga kerakli ozgaruvchilarni yaratamiz 
max_son = None
son_orni = 0
# Sikl yaratamiz n marotaba aylansin 
for i in range(1, n+1):
# Endi for sikli yordamida n marta son qabul qilamiz
    x = int(input())
# if shart kiritamiz x > max_son deb ammo birinchi siklda bu ishlamaydi sababi max_son yoq 
# muammoni yechimi <max_son is None> orqali otib olishi mumkun bu xolatdan.
    if max_son is None or x > max_son:
        max_son = x
        son_orni = i
    elif x==max_son:
        son_orni = i
# Natijani chiqarishda n sonidan max_son ornini yani son_ornini ayrib qoyish kerak boladi 
print(max_son, n-son_orni)        
        



