# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func():

    num_1 = int(input("Enter 1st number: "))
    num_2 = int(input("Enter 2nd number: "))
    num_3 = int(input("Enter 3d number: "))

    num_list = []

    num_list.append(num_1)
    num_list.append(num_2)
    num_list.append(num_3)

    max_num = max(num_list)
    min_num = min(num_list)
    num_list.remove(min_num)

    new_sum = sum(num_list)

    print(new_sum)


my_func()

