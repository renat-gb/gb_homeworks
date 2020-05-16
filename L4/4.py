# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

import collections

num_list = [12, 25, 12, 1, 10, 15, 25, 1, 6, 12, 25, 18, 10, 12]
# Результат должен быть таким: [12, 25, 1, 10, 15, 6, 18]

# Решение без генератора
# res = collections.Counter(num_list)
# print(res.keys())

# print(set(num_list))
# Решение с выводом элементов не по порядку

new_list = []

for el in num_list:
    if el == el:
        num_list.remove(el)

print(num_list)

