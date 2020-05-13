# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def numbers():
    num_a = int(input("Enter 1st number: "))
    num_b = int(input("Enter 2nd number: "))

    if num_b == 0:
        return print("Zero division, start again!")


    result = num_a / num_b
    print(round(result, 2))



numbers()

