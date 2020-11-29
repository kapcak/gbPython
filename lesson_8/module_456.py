'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП.
'''
from abc import ABC
import sys


def show_wh(warehouse=None):
    if warehouse:
        print(warehouse)
    else:
        for wh in all_wh.values():
            print(wh)


def add_to_wh():
    user_input = input("Введите тип техники(1 - принтер, 2 - сканер, 3 - ксерокс):")
    if user_input in add_item.keys():
        item = add_item[user_input].create_item_menu()
        wh = input("Введите склад(адрес)")
        if wh in all_wh.keys():
            all_wh[wh].add_equipment(item)
            print("Успешно добавлено!")
            return
    print("Неверный ввод!")


def remove_from_wh():
    wh_dest = input("Укажите адрес склада(Alaska или Ohio): ")
    if wh_dest in all_wh.keys():
        show_wh(all_wh[wh_dest])
        tech_type = input("Укажите тип техники(1 - принтер, 2 - сканер, 3 - ксерокс): ")
        if tech_type in add_item.keys():
            index = int(input("Укажите индекс элемента: ")) - 1
            if 0 <= index < len(all_wh[wh_dest].equipment[str(add_item[tech_type].__name__)]):
                equip = all_wh[wh_dest].equipment[str(add_item[tech_type].__name__)][index]
                all_wh[wh_dest].remove_equipment(equip)
                return
    print("Неверный ввод!")


def trans_wh():
    wh_source = input("Укажите адрес склада отправителя(Alaska или Ohio): ")
    wh_dest = input("Укажите адрес склада получателя: ")
    if wh_dest in all_wh.keys() and wh_source in all_wh.keys():
        show_wh(all_wh[wh_source])
        tech_type = input("Укажите тип техники(1 - принтер, 2 - сканер, 3 - ксерокс):")
        if tech_type in add_item.keys():
            index = [(int(a) - 1) for a in input("Укажите индексы через пробел").split()]  # список индексов классов
            if len(set(index)) == len(index):
                key = str(add_item[tech_type].__name__)
                tmp_shipment = all_wh[wh_source].equipment[key]  # лист классов
                shipment = [tmp_shipment[id] for id in index if 0 <= id < len(tmp_shipment)]
                WareHouse.transit_equipment(all_wh[wh_source], all_wh[wh_dest], shipment)
                return
    print("Неверный ввод!")


def user_menu():
    print("Выберите операцию:\n"
          "1.Просмотр состояния складов.\n"
          "2.Добавление техники на склад.\n"
          "3.Удаление техники со склада.\n"
          "4.Перемещение техники со склада на склад.\n"
          "0.Выход")
    user_input = input()
    if user_input in ['0', '1', '2', '3', '4']:
        menu[user_input]()
    else:
        user_menu()


class WareHouse:
    def __init__(self, address):
        self.address = address
        self.equipment = {
            "Printer": [],
            "Scaner": [],
            "Xerox": []
        }

    def add_equipment(self, equipment):
        self.equipment[equipment.__class__.__name__].append(equipment)

    def remove_equipment(self, equipment):
        self.equipment[equipment.__class__.__name__].remove(equipment)

    @classmethod
    def transit_equipment(cls, wh_source, wh_dest, shipment):
        for equip in shipment:
            wh_source.remove_equipment(equip)
            wh_dest.add_equipment(equip)

    def __str__(self):
        result = [f'Склад города: {self.address}', '=' * 30]
        for key in self.equipment.keys():
            result.append('-' * 30)
            result.append(f'Элементы типа {key}:')
            for i, el in enumerate(self.equipment[key]):
                result.append(f'{i + 1}.{str(el)}')
        return '\n'.join(result)


class OfficeEquipment(ABC):
    def __init__(self, vendor, model, price):
        self.vendor = vendor
        self.model = model
        self.price = price

    def __str__(self):
        return f'Vendor: {self.vendor} Model: {self.model} Price: {self.price}$'

    @property
    def vendor(self):
        return self.__vendor

    @vendor.setter
    def vendor(self, txt):
        if txt.lower() not in vendors:
            self.__vendor = 'Unknown'
        else:
            self.__vendor = txt

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, dollars):
        dollars = int(dollars)
        if dollars < 0:
            self.__price = 0
        else:
            self.__price = dollars

    @classmethod
    def create_item_menu(cls):
        while True:
            user_input = input("Введите производителя, модель и цену через пробел: ").split()
            if len(user_input) == 3:
                vendor, model, price = user_input
                return cls(vendor, model, price)
            print("Неверный ввод!")


class Printer(OfficeEquipment):
    def __init__(self, vendor, model, price, is_laser=False):
        super().__init__(vendor, model, price)
        self.is_laser = is_laser


class Scaner(OfficeEquipment):
    def __init__(self, vendor, model, price, size='A4'):
        super().__init__(vendor, model, price)
        self.size = size


class Xerox(OfficeEquipment):
    def __init__(self, vendor, model, price, speed=600):
        super().__init__(vendor, model, price)
        self.speed = speed


menu = {
    '1': show_wh,
    '2': add_to_wh,
    '3': remove_from_wh,
    '4': trans_wh,
    '0': sys.exit
}
add_item = {
    '1': Printer,
    '2': Scaner,
    '3': Xerox
}
vendors = [
    'hp',
    'canon',
    'brother',
    'kyocera'
]
Alaska = WareHouse('Alaska')
Ohio = WareHouse('Ohio')
all_wh = {
    "Alaska": Alaska,
    "Ohio": Ohio
}
while True:
    user_menu()
    input("Нажмите Enter для возврата в меню")
