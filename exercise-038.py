"""
Array*. n ta elementdan tashkil topgan a massiv berilgan. Massivda qatnashgan
sonlardan yangi numbers va frequency nomli massiv hosil qiling. numbers massivida
a massividasi sonlardan bittadan olinadi. frequency nomli massivda numbers
massiviga mos ravishda sonlarning takrorlanishlar soni bo'ladi. Massivda qatnashgan
sonlarni va ularni nechatadan qatnashganini aniqlovchi programma tuzilsin. Natijada
har bir son bir marta chiqarilsin.
"""
n = int(input())
A = list(map(int, input().split()))

numbers = []
frequency = []

for x in A:
    if x not in numbers:
        numbers.append(x)
        frequency.append(1)
    else:
        index = numbers.index(x)
        frequency[index] += 1

for i in range(len(numbers)):
    print(numbers[i], frequency[i])