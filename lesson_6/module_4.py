"""
Author: Petrov Yegor
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше
60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:
    def __init__(self, name, color="Черная(ый)"):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def go(self, speed):
        self.speed = int(speed)
        print(f"{self.color} {self.name} движется")
        self.show_speed()

    def stop(self):
        self.speed = 0
        print(f"{self.color} {self.name} останавливается")

    def turn(self, direction):
        print(f"{self.color} {self.name} поворачивает {direction}")

    def show_speed(self):
        if self.speed > 0:
            print(f"{self.color} {self.name} едет со скоростью {self.speed}")
        else:
            print(f"{self.color} {self.name} стоит на месте")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"{self.color} {self.name} превысил(а) скорость!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"{self.color} {self.name} превысил(а) скорость!")


class PoliceCar(Car):
    def __init__(self, name, color="Синяя(ий)"):
        super().__init__(name, color)
        self.is_police = True

diesel = TownCar("Мазда")
gas = PoliceCar("Форд")
shumaher = SportCar("Субару")

racers = [diesel, gas, shumaher]
actions = ["go", "turn", "stop"]
dict = {
    "go": 80,
    "turn": "налево"
}
for action in actions:
    for racer in racers:
        method = getattr(racer, action)
        if action in dict:
            method(dict[action])
        else:
            method()

# for car in racers:
#     car.go(40)
#     car.turn("налево")
#     car.go(80)
#     car.turn("направо")
#     car.show_speed()
#     car.stop()