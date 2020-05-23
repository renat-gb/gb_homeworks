# Реализовать базовый класс Worker (работник)
# Определить атрибуты: name, surname, position (должность), income (доход).

# Последний атрибут должен быть защищенным и ссылаться на словарь
# Элементы словаря: оклад и премия, например, {"wage": wage, "bonus": bonus}.

# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).

# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.worker_name = name
        self.worker_surname = surname
        self.worker_position = position
        self.worker_income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_total_income(self):
        self.wage = sum(self.worker_income.values())
        print(self.wage)

    def get_full_name(self):
        print(self.worker_name, self.worker_surname)


data = Position(name="Alex", surname="Monopoly", position="Doc", wage=12000, bonus=1000)

data.get_total_income()
data.get_full_name()


