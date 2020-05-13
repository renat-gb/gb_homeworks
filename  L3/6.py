# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

new_dict = []


def int_func():
    text = input("Enter any text: ").split(" ")

    for i in range(len(text)):
        dict_keys = text[i].capitalize()
        new_dict.append(dict_keys)

    my_string = " ".join(new_dict)
    print(my_string)


int_func()
