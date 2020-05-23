# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).

# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


class Car:

    def __init__(self, speed, color, name, is_police=True):
        self.car_speed = speed
        self.car_color = color
        self.car_name = name

    def car_go(self):
        print("Car is going ... ")

    def car_stop(self):
        print("Car has stopped ... ")

    def show_speed(self):
        print(f"Speed is: {self.car_speed}")


class TownCar(Car):
    def show_speed(self):
        if self.car_speed >= 60:
            print(f"Speed is: {self.car_speed} too fast!")
        else:
            print(f"Speed is: {self.car_speed}")


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.car_speed >= 40:
            print(f"Speed is: {self.car_speed} too fast!")
        else:
            print(f"Speed is: {self.car_speed}")


class PoliceCar(Car):
    pass


town_car = TownCar(60, "Black", "Town Car")
print(town_car.car_name)
town_car.car_go()
town_car.show_speed()

work_car = WorkCar(30, "White", "Work Car")
print(work_car.car_name)
work_car.car_go()
work_car.show_speed()



