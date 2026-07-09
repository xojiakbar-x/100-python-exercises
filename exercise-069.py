"""
Param12. Elementlari haqiqqiy sonlardan iborat bo’lgan A massiv elementlarining
nomerlarini saqlovchi butun sonlardan iborat, A massiv elementlari o’sish tartibida
joylashtirilgan holdagi elementlar nomerini saqlovchi index nomli massivini hosil
qiluvchi SortIndex(A) protsedurasi tuzilsin. (A massivning o’zi o’zgartirilmasin). index
massivi chiquvchi parametr hisoblanadi
"""
def SortIndex(A):
    index = list(range(len(A)))

    for i in range(len(index)):
        for j in range(i + 1, len(index)):
            if A[index[i]] > A[index[j]]:
                index[i], index[j] = index[j], index[i]

    return index

A = [9, 1, 8, 7, 6]

index = SortIndex(A)

print(index)
print(A)

