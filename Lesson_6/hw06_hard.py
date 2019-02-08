'''
Задание-1: Решите задачу:

Дана ведомость расчета заработной платы (файл "data/workers").
Рассчитайте зарплату всех работников, зная что они получат полный оклад,
если отработают норму часов. Если же они отработали меньше нормы,
то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
удвоенную ЗП, пропорциональную норме.
Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

С использованием классов.
Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
каждый работник получал строку из файла

'''
import os

class Worker:
    def __init__(self, data):
        self.data = dict(zip(['first_name', 'last_name', 'base_salary', 'position', 'hours_norma'], data.split()))
        self.name = f'{self.data["first_name"]} {self.data["last_name"]}'
        self.position = self.data['position']
        self.base_salary = int(self.data['base_salary'])
        self.hours_norma = int(self.data['hours_norma'])
        self.hours_fact = 0

    @property
    def total_salary(self):
        return self.base_salary + self.base_salary / self.hours_norma * (self.hours_fact - self.hours_norma) * (2 if self.hours_fact > self.hours_norma else 1)

    def setFactHours(self, v):
        self.hours_fact = int(v) if v else 0

with open(os.path.join('data/workers'), 'r') as f_w, open(os.path.join('data/hours_of'), 'r') as f_h:
    # парсим hours_of, получаем структуру {человек: часы}
    hours = {f'{s.split()[0]} {s.split()[1]}': s.split()[2] for s in f_h.readlines()[1:]}
    # описываем классы по файлу workers
    print("Работник, должность, оклад, норма часов, отработано, заработок")
    for s in f_w.readlines()[1:]:
        w = Worker(s)
        # добавляем в него фактически отработанные часы
        w.setFactHours(hours.get(w.name))
        print(f"{w.name:<25} {w.position:<15} {w.base_salary:^10} {w.hours_norma:^5} {w.hours_fact:^5} {w.total_salary:^15.2f}")