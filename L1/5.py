cash_in = int(input("Введите выручку: "))
cash_out = int(input("Введите издержки: "))

if cash_in > cash_out:
    print("Вы работаете в прибыль")
    rent = (cash_in / cash_out) * 100
    print(f"Рентабельность: {rent} %")
else: print("Вы работаете в убыток")

workers = int(input("Сколько сотрудников в компании? "))

profit = cash_in - cash_out

profit_one = profit / workers

print(f"Прибыль на сотрудника: {profit_one}")

# Могут быть проблемы с пониманием рентабельности, в целом считаю, что механика кода работает исправно