# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

import itertools

new_list = ["a", "b", "c"]

i = 0

for item in itertools.cycle(new_list):
    if i > 50:
        break
    else:
        print(item)
        i = i + 1

