# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий
# по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.


import re

sum_list = []

with open("6_sett.txt", "r") as doc:
    for line in doc:
        dig = re.findall("\d+", line)

        science_list = ["Информатика: ", "Физика: ", "Физкультура: "]
        result = [int(item) for item in dig]
        final_result = sum(result)
        sum_list.append(final_result)

    for predmet, number in zip(science_list, sum_list):
        print(predmet, number)


