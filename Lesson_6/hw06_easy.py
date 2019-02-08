'''
Задача-1: Написать класс, например, Worker, который должен содержать информацию
о работнике (ФИО, оклад, надбавка за напряженность).
Создать экземпляр класса и передать конкретные данные (примеры ФИО, должности,
оклад и надбавки). Оклад и надбавку передать в виде строки.
На основе строки создать атрибут income, который реализовать в виде словаря
и инкапуслировать. Словарь income должен содержать информацию об окладе и надбавке.
Применить к экземпляру
класса метод __dict__ и проверить какой будет результат применения этого метода.
А комментариях к заданию написать тип результата на русском языке.
'''

# Структура работников
class Worker:
    def __init__(self, name, surname, middleName, salary, addition):
        self.name = name
        self.surname = surname
        self.middleName = middleName
        self.salary = int(salary)
        self.addition = int(addition)
        self.__income = {'salary': self.salary, 'bonus': self.addition}

driver = Worker('Валенков', 'Валерий', 'Игоревич', '55000', '5000')
collector = Worker('Котов', 'Борис', 'Иванович', '40000', '2000')
packer = Worker('Лазарева', 'Екатерина', 'Михайловна', '38000', '7000')

print(type(driver.__dict__), driver.__dict__)
# Тип словарь, данные в виде ключ-значение

'''
Задача-2: Продолжить работу над задачей 1. Создать на основе класса Worker класс
Position (реализовать наследование). Добавить классу уникальный атрибут -
% премии к зарплате (от суммы оклада).
Создать метод расчета зарплаты с учетом только премии.
Реализовать обращение к этому атриубуту, как к свойству.
Проверить работу всей структуры на реальных данных, вывести результаты.
'''

class Position(Worker):
    def __init__(self, name, surname, middleName, salary, addition, bonus, date_of_birth):
        Worker.__init__(self, name, surname, middleName, salary, addition)
        self.bonus = int(bonus)
        self.date_of_birth = date_of_birth

    @property
    def calculateBonus(self):
        return self.salary + self.salary * self.bonus / 100

    def getFIO(self):
        return self.name + ' ' + self.surname + ' ' + self.middleName + ', дата рождения: ' + self.date_of_birth

    def getTotalSalary(self):
        return self.calculateBonus + self.addition

driver_position = Position('Звякин', 'Сергей', 'Борисович', '40000', '3000', '10', '10.04.1985')
print('Зарплата с учетом премии:', driver_position.calculateBonus)

'''
Задача-3: Продолжить работу над задачей 2.  Реализовать полиморфизм
использования знака + в методах 1) вывода полного имени работника и возраста
2) вычисления общего дохода работника с учетом надбавки .
Проверить работу всей структуры на реальных данных, вывести результаты.
'''

print(driver_position.getFIO())
print('Итоговая зарплата:', driver_position.getTotalSalary())