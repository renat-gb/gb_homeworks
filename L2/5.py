my_list = [int(num) for num in input("Введите элементы рейтинга через запятую: ").split(",")]
print(my_list)
print(type(my_list))


new_rate = int(input("Введите новый элемент рейтина: "))

new_list = []
add_list = []
rate_list = [new_rate]

for i in my_list:
    if i < new_rate:
        new_list.append(rate_list + my_list)
        print(new_list)
        break
    if i > new_rate:
        new_list.append(my_list + rate_list)
        print(new_list)
        break

    else:
        print(new_list)
        break
# Не могу понять как вставить rate_list в определенную позицию списка.
# Нужно как-то определить пересекающийся индекс и по нему вставлять.




