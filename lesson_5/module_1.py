"""
Author: Petrov Yegor
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open("files/1.txt", "w") as file:
    while True:
        user_input = input("Введите строку: ")
        if user_input == "":
            break
        print(user_input, file=file)