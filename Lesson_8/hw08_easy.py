"""
Задание 1. Реализовать класс-строитель. В его конструктор передать два списка.
Класс должен возвратить python-объект словарь. Проверить, что объект
создается корректно - создать экземпляр класса и обратиться к значению
элемента словаря, как к атрибуту класса.
"""


class DictBuild:
    def __init__(self, keys, values):
        [setattr(self, keys[i], values[i]) for i in range(min(len(keys), len(values)))]

    def __getattr__(self, item):
        return f'key {item} not found'


l1_keys = ['programmer', 'director', 'manager', 'driver']
l2_values = [100000, 150000, 50000, 55000, 60000]

print(DictBuild(l1_keys, l2_values).programmer)

'''
Задание 2.
Создать класс-обертку для списка. Список передвайте в конструктор класса.
Реализуйте удаление всех элементов из списка через функцию clear.
Но функция должна применяться не к списку, а к экземпляру класса.
Внутри класса должно быть предусмотрено делегирование этой функции методу (clear)
списка.
'''


class Positions:
    def __init__(self, _pos):
        self.names = _pos

    def __getattr__(self, item):
        return getattr(self.names, item)


positions = Positions(['programmer', 'director', 'manager', 'driver'])
positions.clear()
print(positions.names)
