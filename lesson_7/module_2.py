'''
Author: Petrov Yegor
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
'''
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = int(size)

    @abstractmethod
    def count_materials(self):
        pass

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 1:
            self.__size = 1
        elif size > 70:
            self.__size = 70
        else:
            self.__size = size


class Coat(Clothes):
    materials = 0  # Сведения о размерах всех пальто

    def __init__(self, size):
        super().__init__(size)
        Coat.materials += self.size

    def count_materials(self):
        return round(self.size / 6.5 + 0.5, 2)

    @staticmethod
    def count_all_materials():
        return round(Coat.materials / 6.5 + 0.5, 2)


class Suit(Clothes):
    materials = 0  # Сведения о размерах всех костюмов

    def __init__(self, size):
        super().__init__(size)
        Suit.materials += self.size

    def count_materials(self):
        return round(2 * self.size + 0.3, 2)

    @staticmethod
    def count_all_materials():
        return round(2 * Suit.materials + 0.3, 2)


coat_a = Coat(10)
# Для одного экземпляра класса, текущий и общий расход ткани равны
print(coat_a.count_materials())  # 2.04
print(Coat.count_all_materials())  # 2.04

coat_b = Coat(20)
# При двух экземплярах общий расход больше
print(coat_b.count_materials())  # 3.58
print(Coat.count_all_materials())  # 5.12

# @property не дает выходить за границы значений
suit_a = Suit(130)
print(suit_a.size)  # 70
print(suit_a.count_materials())  # 140.3

# @property не дает выходить за границы значений
suit_b = Suit(-50)
print(suit_b.size)  # 1
print(Suit.count_all_materials())  # 142.3
