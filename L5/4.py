# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

import re

russian = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

new_dic = []

with open("4_sett.txt", "r") as doc:
    for el in doc:
        res = el.replace("\n", "")

        number = re.findall("\d+", res)
        new_dic.append(number[0])


for i, n in zip(new_dic, russian.values()):
    print(f"{n} - {i}")


with open("4_sett_new.txt", "w") as doc_new:
    for i, n in zip(new_dic, russian.values()):
        doc_new.write(n)
        doc_new.write(" - ")
        doc_new.write(i)
        doc_new.write("\n")

# В качестве хитрого и короткого решения, можно установить модуль googletrans
# И просто перевести строки на русский язык в одну строку

