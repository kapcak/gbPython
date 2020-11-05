'''
Author: Petrov Yegor
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
'''
def user_input(rating):
    a = int(input("Введите новый элемента рейтинга (положительное целое число): "))
    notset = True
    for i, el in enumerate(list(rating)):
        if a > el:
            rating.insert(i, a)
            notset = False
            break
    if notset:
        rating.append(a)
    return rating

a = int(input("Введите первый элемент рейтинга: "))
rating = [a]
counter = 0
while counter < 5:
    rating = user_input(rating)
    counter += 1
print(rating)
