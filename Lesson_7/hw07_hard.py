'''
Задача-1: Написать класс Command. В конструктор класса передать переменную
positions. Она будет содержать список с должностями. В конструкторе класса
определить эту переменную как атрибут класса и АБСОЛЮТНО инкапсулировать.
Переопределить методы __len__ и __contains__ класса. Метод __len__ должен
выводит сообщение о переопределении метода и размер списка. Метод __contains__
должен выводить очередной элемент из списка. (не забудьте этот элемент
передать в сам метод). Создать экземпляр класса с данными. В экземпляр передать
список. Проверить работу методов. Второй метод будет проверять, входит ли
элемент в список
'''

class Command:
    def __init__(self, position):
        self.__position = position

    def __len__(self):
        return f'Переопределенный метод len, длина: {len(self.__position)}'

    def __contains__(self, item):
        return f'{item} {"" if item in self.__position else "не "}является элементом списка'

command = Command(['driver', 'programmer', 'director', 'manager', 'decorator'])

print(command.__len__())
print(command.__contains__('programmer'))
print(command.__contains__('doctor'))

'''
Переопределенный метод len, длина: 5
programmer является элементом списка
doctor не является элементом списка
'''