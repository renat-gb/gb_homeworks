# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def data_set():
    data_name = input("Enter your name: ")
    data_surname = input("Enter your surname: ")
    data_year = int(input("Enter your birthday year: "))
    data_city = input("Enter your living city: ")
    data_email = input("Enter your email: ")
    data_phone = input("Enter your phone: ")

    age = 2020 - data_year

    print(f"Hello {data_name} {data_surname}! I think you are {age} years old. You live in {data_city}. "
          f"Your email is {data_email}, and your phone number is {data_phone} ")

data_set()




































