"""
Author: Petrov Yegor
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce

def multiply(prev_el, el):
    return prev_el * el

list = [even for even in range(100, 1001) if not even % 2]
print(reduce(multiply, list))