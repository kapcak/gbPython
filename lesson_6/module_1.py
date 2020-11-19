"""
Author: Petrov Yegor
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color
(цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках метода
реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) —
2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу
примера, создав экземпляр и вызвав описанный метод.
"""
import time

RED = 7
YELLOW = 2
GREEN = 5

class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self):
        self.__color = "красный"
        print(f"На светофоре загорелся {self.__color}")
        time.sleep(RED)

        self.__color = "желтый"
        print(f"На светофоре загорелся {self.__color}")
        time.sleep(YELLOW)

        self.__color = "зеленый"
        print(f"На светофоре загорелся {self.__color}")
        time.sleep(GREEN)

light = TrafficLight()

while input("Для активации светофора нажмите Enter") == '':
     light.running()