'''
Задача-1: Реализовать индексацию элементов списка не с нуля, а с 5, т.е. 5, 6, 7
и т.д.
'''

class IterObj:
    def __init__(self, start = 0, value = 0):
        self.i = start
        self.value = value

    def __next__(self):
        self.i += 1
        if self.i <= self.value: return self.i
        else: raise StopIteration

class Iter:
    def __init__(self, start = 0, value = 0):
        self.value = value
        self.start = start - 1
    def __iter__(self):
        return IterObj(self.start, self.value)

obj = Iter(5, 7)
for el in obj:
    print(el)

'''
Задача-2: Придумать любу структуру данных. Она должна содержать два атрибута.
Значение одного атрибута передается в конструктор, а значение другого - определяетсяъ
прямо в конструкторе класса. Для этой структуры данных написать метод,
который должен выполнять какой-то функционал. Создать экземпляр класса, передать
данные. Вызывать метод. Проверить, что находится в переменной-экземпляре класса.
Переопределить метод __str__. Этот метод должен возвращать тот результат,
который вы захотите. Проверить еще раз. В комментарии написать, в чем разница
между подходом с использованием метода __str__ и без него.
'''

class Persimmon:
    def __init__(self, color):
        self.color = color
        self.name = 'хурмушенька'

    def description(self):
        self.name = self.name + '!'
    def __str__(self):
        return f'{self.name}, цвет: {self.color}!'

    @staticmethod
    def getType(obj):
        return f'Тип: {type(obj)}'

persimmon = Persimmon('красная')
print(persimmon)

# стандартный вывод отобразит объект с ссылкой на область памяти <__main__.Persimmon object at 0x101b67470>
# при использовании перегрузки метода, возможно заменить стандартный вывод на желаемый результат

'''
Задача-3: Продолжить работу над задачей 2. Добавить еще один метод. Он должен
вывзваться из экземпляра класса. В этот метод нужно передать некое значение.
Сам метод должен ловить значение и что-то с ним делать и возвращать результат.
Реализовать для этого метода декоратор @staticmethod
'''
print(persimmon.getType(obj))



