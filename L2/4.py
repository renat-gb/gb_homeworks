new_list = input("Введите несколько слов через пробел: ").split(" ")

print(new_list)
print(type(new_list))


for i in range(len(new_list)):
    final = new_list[i]
    print(i + 1, final[:9])


