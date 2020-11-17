"""
Author: Petrov Yegor
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum."""

with open("files/2.txt", "r+") as file:
    for line in text:
        file.writelines(line)
    file.seek(0)
    counter = 0
    for string in file:
        counter += 1
        print(f"В строке {counter} {string.count(' ') + 1} слов.")
    print(f"Всего в файле {counter} строк.")