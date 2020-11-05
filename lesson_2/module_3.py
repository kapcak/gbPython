'''
Author: Petrov Yegor
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''
user_month = int(input("Введите номер месяца: "))

# dict
time_of_year = {
    "Зима": [1, 2, 12],
    "Весна": [3, 4, 5],
    "Лето": [6, 7, 8],
    "Осень": [9, 10, 11]
}
for times, months in time_of_year.items():
    if user_month in months:
        print(f"{times} (словарь)")

# list
months = [
    [1, 2, 12],
    [3, 4, 5],
    [6, 7, 8],
    [9, 10, 11]
]
while(True):
    if user_month in months[0]:
        print("Зима (список)")
        break
    if user_month in months[1]:
        print("Весна (список)")
        break
    if user_month in months[2]:
        print("Лето (список)")
        break
    if user_month in months[3]:
        print("Осень (список)")
        break
