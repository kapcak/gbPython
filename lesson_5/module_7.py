"""
Author: Petrov Yegor
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать
данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить
ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
from json import dump

d_profit = {}
with open("files/7.txt", "r") as file:
    sum_profit = 0
    prof_firms = 0
    for line in file:
        l = line.split()
        l[2], l[3] = int(l[2]), int(l[3])
        profit = l[2] - l[3]
        if profit >= 0:
            print(f"{l[0]} показала прибыль в размере {profit}")
            sum_profit += profit
            prof_firms += 1
        else:
            print(f"{l[0]} терпит убытки в размере {profit}")
        d_profit[l[0]] = profit
average_profit = sum_profit / prof_firms
print(f"Средняя прибыль составила: {average_profit}")
result = [d_profit, {"average_profit": average_profit}]
with open("files/result.json", "w") as file:
    dump(result, file)