# Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.


dic = []

import re
import json

with open("7_sett.txt", "r") as doc:
    for firm in doc:
        text_line = firm.replace("\n", "")
        # print(text_line)

        number = re.findall("\d+", text_line)
        # print(number)
        del number[0]
        # print(number)

        firm_number = number[0]

        cash_in = int(number[1])
        # print(f"Доход: {cash_in}")

        cash_out = int(number[2])
        # print(f"Расход {cash_out}")

        cash_res = cash_in - cash_out
        # print(f"Прибыль {firm_number}й компании: {cash_res}")
        # print("_"*50)

        dict_new = {
            f"firm_{firm_number}": cash_res
        }

        # print(dict_new)

        dic.append(dict_new)


print(dic)


with open("7_dict.json", "w") as final_one:
    json.dump(dic, final_one)













