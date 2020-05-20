# Создать текстовый файл (не программно), сохранить в нем несколько строк.
# Выполнить подсчет количества строк, количества слов в каждой строке.


with open("text_in", "r") as f:
    for line in f:

        dl = len(line)
        new_dl = (dl - 1)
        line_word = line.replace("\n", " ")

        result = f"Длина слова {line_word}равна: {new_dl} символ(ов)"
        print(result)

print("_"*50)

with open("text_in", "r") as f:
    n_list = f.readlines()

n_dict = []

for keys in n_list:
    number = keys.count("\n")
    n_dict.append(number)

final_res = sum(n_dict)

print(f"Количество строк в файле: {final_res}")


# Открывать файл на чтение 2 раза было не обязательно, работа выполнялась блоками.

