# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
n = int(input('Введите число: '))

def fibonacci(n):
    fib_numbers = []
    a, b = 1, 1
    for i in range(n-1):
        fib_numbers.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fib_numbers.insert(0, a)
        a, b = b, a - b
    return fib_numbers

fib_numbers = fibonacci(n)
print(fibonacci(n))
print(fib_numbers.index(0))