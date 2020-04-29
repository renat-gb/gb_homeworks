num = int(input("Введите месяц в виде целого числа от 1 до 12: "))

zima = [12, 1, 2]
vesna = [3, 4, 5]
leto = [6, 7, 8]
osen = [9, 10, 11]

if num in zima:
    print("Сейчас зима!")
if num in vesna:
    print("Сейчас весна!")
if num in leto:
    print("Сейчас лето!")
if num in osen:
    print("Сейчас осень!")

