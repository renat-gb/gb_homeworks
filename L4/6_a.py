# Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

import itertools

num = int(input("End point is 100. Enter number to start with: "))

for i in itertools.count(num):
    if i > 100:
        break
    else:
        print(i)

# Итератор не сдал делать бесконечным намеренно. Ограничил до 100


