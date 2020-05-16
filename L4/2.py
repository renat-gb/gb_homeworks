# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
#
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.

import random

my_list = []
i = 0
while i < 10:
    num = random.randint(1, 100)
    my_list.append(num)
    i = i + 1

print(my_list)

new_list = []

for i in range(len(my_list)):
    if my_list[i] > my_list[i - 1]:
        new_list.append(my_list[i])

print(new_list)

