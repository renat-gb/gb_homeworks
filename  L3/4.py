# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# def my_func(x, y):
#     y = abs(y)
#     res = x ** y
#     print(res)
# my_func(2, -8)


def my_func(x, y):
    y = abs(y)

    n = 1
    while y > 0:
        n = n * x
        y = y - 1

    print(n)


my_func(2, -3)
