'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''


class Complex:
    def __init__(self, a, i):
        self.a = a  # Действительная часть
        self.i = i  # Мнимая часть

    def __str__(self):
        if self.i > 0:
            return f'{self.a}+{self.i}i'
        else:
            return f'{self.a}{self.i}i'

    def __add__(self, other):
        return Complex(self.a + other.a, self.i + other.i)

    def __mul__(self, other):
        return Complex((self.a * other.a - self.i * other.i), (self.i * other.a + self.a * other.i))


z_1 = Complex(1, 3)
z_2 = Complex(4, -5)
print(f'z_1 = {z_1}')
print(f'z_2 = {z_2}')
print(f'z_1 + z_2 = {z_1 + z_2}')
print(f'z_1 * z_2 = {z_1 * z_2}')
