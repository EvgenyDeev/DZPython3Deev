# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randint


number = int(input('Введите размер списка: '))
list_one = []
list_two = []

for i in range(number):
    list_one.append(randint(1, 10))

for i in range(len(list_one)):
    while i < len(list_one)/2 and number > len(list_one)/2:
        number = number - 1
        a = list_one[i] * list_one[number]
        list_two.append(a)
        i += 1

print(f"Первоначальный список: {list_one}")
print(f"Произведение пар из списка: {list_two}")