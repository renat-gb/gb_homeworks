num = int(input("Введите целое положительное число: "))
res = num % 10
num = num // 10
while num > 0:
    if num % 10 > res:
        res = num % 10
    num = num // 10

print(f"Самая большая цифра в числе: {res}")