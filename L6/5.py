# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
#
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
#
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title=None):
        self.stationery_title = title

    def draw(self):
        print("Запуск отрисовки ... ")


class Pen(Stationery):
    def draw(self):
        print("Ручка начинает писать ...")


class Pencil(Stationery):
    def draw(self):
        print("Карандаш начинает писать ...")


class Handle(Stationery):
    def draw(self):
        print("Маркер начинает писать ... ")


st_main = Stationery()
st_main.draw()

st_handle = Handle()
st_handle.draw()

st_pen = Pen()
st_pen.draw()

st_pencil = Pencil()
st_pencil.draw()


