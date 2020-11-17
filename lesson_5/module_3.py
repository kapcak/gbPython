"""
Author: Petrov Yegor
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести
фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""
with open("files/3.txt", "r+", encoding="UTF-8") as file:
    # while True:
    #     user_input = input("Введите фамилию и оклад сотрудника (пустая строка для выхода из режима ввода): ")
    #     if user_input == "":
    #         break
    #     file.write(f"{user_input}\n")
    # file.seek(0)
    print("Зарплата меньше 20000:")
    sum = 0
    counter = 0
    for line in file:
        list = line.split()
        sum += int(list[1])
        if int(list[1]) < 20000:
            print(list[1])
        counter += 1
    print(f"Средняя заработная плата сотрудников: {sum / counter:.2f}")
