"""
Author: Petrov Yegor
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
lines =[]
enru = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
}
with open("files/4.txt", "r+", encoding="UTF-8") as file:
    for line in file:
        lines.append(list(line.split()))
    file.seek(0)
    for i, word in enumerate(lines):
        lines[i][0] = enru[word[0]]
        print(" ".join(lines[i]), file=file)