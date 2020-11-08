"""
Author: Petrov Yegor
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

def my_func(a, b, c):
    if a > b:
        if b > c:
            return a + b
        return a + c
    if a > c:
        return a + b
    return b + c

a, b, c = input("Введите 3 числа: ").split()
print(f"Сумма наибольших равна: {my_func(int(a), int(b), int(c))}")