# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# Программа расчитана на любое количество сотрудников. Файл 3_sett.txt можно дополнить данными.

import re

# Блок вычисления ЗП меньше 20.000
with open("3_sett.txt", "r") as f:
    print("Results: ")
    for line in f:

        num_sep = line.replace("\n", "")
        result = re.split(r":", num_sep)

        name = result[0]
        salary = int(result[1])

        new_dic = {name: salary}

        for val in new_dic.values():
            if val < 20000:
                for i in new_dic.items():
                    print(i)

print("_" * 50)

# Кусок кода из второго задания, на случай, если количество сотрудников заранее не известно
# Если известно, достаточно использовать фиксированное число
with open("3_sett.txt", "r") as f:
    n_list = f.readlines()
n_dict = []
for keys in n_list:
    number = keys.count("\n")
    n_dict.append(number)
final_res = sum(n_dict)
print(f"Количество сотрудников: {final_res}")


# Блок подсчета средней заработной платы
with open("3_sett.txt", "r") as f:

    salary_list = []
    for number in f:
        num_only = number.replace("\n", "")
        salary_all = re.findall("\d+", num_only)
        salary_all_int = int(salary_all[0])
        salary_list.append(salary_all_int)

final_summary = sum(salary_list)
print(f"Общая заработная плата: {final_summary}")
div_res = final_summary / final_res

print(f"Средняя величина дохода сотрудников: {div_res}")

