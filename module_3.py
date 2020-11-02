'''
Author: Petrov Yegor
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''
digits = int(input("Пожалуйста, введите число: "))
result = digits + int(str(digits)*2) + int(str(digits)*3)
print(result)
