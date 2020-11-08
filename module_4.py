"""
Author: Petrov Yegor
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""

def my_func(base, exp):
    i = abs(exp)

    # Альтернативный путь
    # return 1 / base ** i

    counter = 1
    temp = base
    while counter < i:
        temp *= base
        counter += 1
    return 1 / temp

base, exp = input("Введите действительное и целое отрицательное числа: ").split()
base = float(base)
exp = int(exp)
print(my_func(base, exp))