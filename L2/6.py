num = int(input("Количество товаров в каталоге: "))
print(f"Количество товаров: {num} ")

names_list = []
price_list = []
amount_list = []
count_type_list = []

i = 1
while i <= num:
    print(f"Введите характеристики {i}го товара")
    i += 1

    dict1 = {}
    name = input("Введите название: ")
    price = int(input("Введите цену: "))
    amount = int(input("Введите количество: "))
    count_type = input("Введите единицу измерения: ")

    dict1["Название: "] = name
    dict1["Цена: "] = price
    dict1["Количество: "] = amount
    dict1["Ед: "] = count_type


    names_list.append(name)
    price_list.append(price)
    amount_list.append(amount)
    count_type_list.append(count_type)

final_dic = {
    "<Название>": names_list,
    "<Цена в руб>": price_list,
    "<Количество>": amount_list,
    "<Единица измерения>": count_type_list

}

print("Результаты статистики: ")
list(map(print, final_dic.keys(), final_dic.values()))










































