# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12
from random import randint
numbers = []
for i in range(5):
    numbers.append(randint (0,11))
summ = 0
for i in range(1, len(numbers), 2):
        summ += numbers[i]       
print(f"Наш список: {numbers}", f"сумма элементов на нечётных позициях: {summ} ")