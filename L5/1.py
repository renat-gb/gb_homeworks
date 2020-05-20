# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

text_in = input("Enter any text with space: ").split(" ")
# print(text_in)


with open("text_in", "w") as f:
    for line in text_in:
        f.write(line + "\n")

