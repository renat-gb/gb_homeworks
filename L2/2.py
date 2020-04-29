num = [int(x) for x in input("Введите числа через запятую: ").split(",")]

print(num)
print(type(num))

# num = [1, 2, 3, 4, 5]
# num = [1, 2, 3, 4,]


if len(num) % 2 == 0:
    i = 0
    while i < len(num):
        nlist = num[i]
        num[i] = num[i+1]
        num[i+1] = nlist
        i += 2

else:
    i = 0
    while i < len(num) - 1:
        nlist = num[i]
        num[i] = num[i+1]
        num[i+1] = nlist
        i += 2


print(num)

