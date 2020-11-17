"""
Author: Petrov Yegor
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
и выводить ее на экран.
"""
from random import random

with open("files/5.txt", "w") as file:
    amount = int(input("Введите желаемое кол-во чисел: "))
    for number in range(amount):
        file.write(f"{str(int(random() * 1000))} ")

with open("files/5.txt", "r") as file:
    digits = [int(digit) for digit in file.readline().split()]
    print(sum(digits))