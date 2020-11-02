"""
Author: Petrov Yegor
1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

some_digits, some_other_digits = 0, 0 # Создаем несколько пустых числовых переменных
some_string, some_other_string = "", "" # Создаем несколько пустых строковых переменных

# Присвоим значения и выведем на экран
some_digits = 50.0
some_string = "Какая-то невнятная строка"
print(f"В переменной some_digits хранится значение {some_digits}, ее тип {type(some_digits)}")
print(f"В переменной some_string хранится значение {some_string}, ее тип {type(some_string)}")

# Позволим пользователю ввести значения в другие переменный и выведем их
some_other_digits = int(input("Пожалуйста введите целое число: "))
some_other_string = input("Пожалуйста, введите строку: ")
print(f"Ваше число: {some_other_digits}")
print(f"Ваша строка: {some_other_string}")
