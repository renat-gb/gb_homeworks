# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time


class TrafficLight:
    def __init__(self, _color):
        self.color = _color


running_red = TrafficLight(_color="Red")
running_yell = TrafficLight(_color="Yellow")
running_green = TrafficLight(_color="Green")

print(running_red.color)
time.sleep(7)
print(running_yell.color)
time.sleep(2)
print(running_green.color)
time.sleep(5)
