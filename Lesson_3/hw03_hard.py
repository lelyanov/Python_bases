# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

print('Задание 1')

# Функция округления значения
def rounding(value, n):
    _head, _out = str(value).split('.')
    check = lambda x: 1 if x >= 5 else 0
    if len(_out) > n:
        new_out = int(_out[:n]) + check(int(_out[n]))
        if len(_out[:n]) != len(str(new_out)):
            _head = int(_head) + 1
        return (str(_head) + '.' + str(new_out)[-n:])
    else:
        return _head + '.' + _out[:n]

print(rounding(5.4999937, 4))
print(rounding(6.9999967, 5))
print(rounding(8.1999961, 5))
print(rounding(1.3333322343, 6))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

print('Задание 2')

# Парсер строки
def parser(data_str):
    data_list = data_str.split(' ')
    while data_list.count('') > 0: data_list.remove('')
    return data_list

# Расчет колонки total
def calculateTotalSalary(data):
    if data['clock_fact'] == data['clock_rate']:
        return data['salary']

    pay_in_hour = data['salary']/data['clock_rate']
    if data['clock_fact'] < data['clock_rate']:
        return data['salary'] - (data['clock_rate'] - data['clock_fact']) * pay_in_hour
    elif data['clock_fact'] > data['clock_rate']:
        return data['salary'] + (data['clock_fact'] - data['clock_rate']) * pay_in_hour * 2

# Расчет табеля
def read_files(file_workers, file_hours):
    # Заполним таблицу по штатке
    workers_list = []
    with open(file_workers, 'r', encoding='utf-8') as file:
        for w in file.readlines()[1:]:
            worker = parser(w)
            if len(worker) != 5 or worker is None: continue
            workers_list.append({'f_name': worker[0], 'l_name': worker[1], 'salary': int(worker[2]), 'position': worker[3], 'clock_rate': int(worker[4]), 'clock_fact': 0, 'total': 0})

    # Получим фактические значения
    hours_list = []
    with open(file_hours, 'r', encoding='utf-8') as file:
        for h in file.readlines()[1:]:
            hours_data = parser(h)
            if len(hours_data) != 3: continue
            hours_list.append({'f_name': hours_data[0], 'l_name': hours_data[1], 'clock_fact': int(hours_data[2])})

    # Объединим данные
    for i in hours_list:
        find_worker = list(filter(lambda x: (x['l_name'] == i['l_name'] and x['f_name'] == i['f_name']), workers_list))
        if not find_worker is None:
            find_worker[0]['clock_fact'] = i['clock_fact']
            find_worker[0]['total'] = calculateTotalSalary(find_worker[0])

    return workers_list

workers = read_files(file_workers='data//workers', file_hours='data//hours_of')
[print(cell) for cell in workers] # Итоговая сумма оплаты в колонке 'total'

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

print('Задание 3')

# Сортировка информации по группам
def fruits_list_work3(fruits):
    # createfile - Создание файла с данными
    def createfile(fruits, file_name):
        with open(f'data//fruits_{file_name}.txt', 'w', encoding='utf-8') as file:
            for fruit in fruits:
                file.write(fruit)
    new_fruits = []
    last_group = ''
    for fruit in fruits:
        if last_group != fruit[0]:
            if len(new_fruits) > 0:
                createfile(new_fruits, last_group)
                new_fruits.clear()
            last_group = fruit[0]
        new_fruits.append(fruit)
    if len(new_fruits) > 0: createfile(new_fruits, last_group)

# Чтение общего списка фруктов
def read_file_work3(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        fruits_list = []
        for w in file.readlines()[1:]:
            if len(w) == 1:
                continue
            fruits_list.append(w)
        fruits_list.sort()
        fruits_list_work3(fruits_list)

read_file_work3('data//fruits.txt')
print('Сортировка завершена!')