"""
Array116. n ta elementdan tashkil topgan A massiv berilgan. Seriya deb, ketma – ket
kelgan bir hil elementlar guruhida aytiladi. Seriya uzunligi esa, bu elementlar soni.
(seriya uzunligi 1 bo’lishi mumkin). Butun sonlardan iborat bo’lgan, elementlar soni bir
xil bo’lgan B va C massivni hosil qiling. B massivga A massivdagi seriyalar uzunligi, C
massivga esa seriyani tashkil qilgan element qiymatini yozing
"""
n = int(input())
A = list(map(int, input().split()))

B = []
C = []

i = 0

while i < n:
    count = 1

    while i + 1 < n and A[i] == A[i + 1]:
        count += 1
        i += 1

    B.append(count)
    C.append(A[i])

    i += 1

print(*B)
print(*C)


