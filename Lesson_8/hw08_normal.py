"""
Задание_1. Создать класс. В конструктор передать два параметра - два числа.
Создать второй класс. В конструкторе первого предусмотреть создание
объекта второго класса. Кроме того, в первом классе предусмотреть три метода,
в которых делегировать получение остатка от деления, результата деления и целой
части от деления в методы второго класса (предусмотреть вычисление в соотв. методах
второго класса).
"""


class Class_1:
    def __init__(self, v1, v2):
        self.class_2 = Class_2(v1, v2)

    def __getattr__(self, item):
        return getattr(self.class_2, item)


class Class_2:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def moddiv(self):
        return self.v1 % self.v2

    def div(self):
        return self.v1 / self.v2

    def intdiv(self):
        return self.v1 // self.v2


test_class = Class_1(45, 2)
print(test_class.moddiv())
print(test_class.div())
print(test_class.intdiv())
