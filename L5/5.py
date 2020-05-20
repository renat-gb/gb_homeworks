# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open("5_sett.txt", "w") as doc:
    num_list = [int(x) for x in input("Введите числа через пробел: ").split(" ")]
    print(num_list)
    summa = sum(num_list)
    print(f"Сумма чисел в списке: {summa}")

    for i in num_list:
        doc.writelines(str(i))
        doc.writelines(", ")

