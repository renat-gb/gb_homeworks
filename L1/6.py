a = int(input("Введите количество километров А: "))
b = int(input("Введите количество километров В: "))

c = 1
if a > b:
    print(c)

while a < b:
    a = a + (a / 10)
    c = c + 1

print(c)


