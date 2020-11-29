'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''


class Date:
    regular_year = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    leap_year = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    def __init__(self, date: str):
        self.date = date

    @classmethod
    def get_date(cls, param):
        day, month, year = [int(a) for a in param.date.split('-')]
        return day, month, year

    @staticmethod
    def check_date(day, month, year):
        for el in (day, month, year):
            if not isinstance(el, int) and el < 0:
                return False
        if year % 4 == 0:
            if month in Date.leap_year.keys():
                if day <= Date.leap_year[month]:
                    return True
        elif month in Date.regular_year.keys():
            if day <= Date.regular_year[month]:
                return True
        return False


new_date = Date('29-02-2019')

print(Date.get_date(new_date))
print(Date.check_date(*Date.get_date(new_date)))
