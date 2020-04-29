num = int(input("Введите месяц в виде целого числа от 1 до 12: "))

months = {
    1: "Январь - это зима",
    2: "Февраль - это зима",
    3: "Март - это весна",
    4: "Апрель - это весна",
    5: "Май - это весна",
    6: "Июнь - это лето",
    7: "Июль - это лето",
    8: "Август - это лето",
    9: "Сентябрь - это осень",
    10: "Октябрь - это осень",
    11: "Ноябрь - это зима",
    12: "Декабрь - это зима"
}

for i in months:
    if i == num:
        if i <= 3 or 5:
            print(months.get(i))
            break
    if i == num:
        if i <= 6 or 8:
            print(months.get(i))
            break
    if i == num:
        if i <= 9 or 11:
            print(months.get(i))
            break
    if i == num:
        if i == 12 or 1 or 2:
            print(months.get(i))
            break