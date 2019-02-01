# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
import random
import re

print('Задание 1')
_str = 'mtMmEZUOmcqKFcxeKDDAfFFSwwFgg'

# поиск с использование пакета re
def re_filter(str_in):
    regex = '(?:[A-Z]+)*(?P<target>[a-z]+)(?:[A-Z]+)*'
    return re.findall(regex, str_in)

# поиск стандартными средствами
def notRe_filter(str_in):
    _str2 = ''
    for i in range(ord('A'), ord('Z')+1):
        _str2 += chr(i)

    res_list = []
    last_v = ''
    i = 0
    check_length = lambda: res_list.append(last_v) if len(last_v) > 0 else False
    while i < len(str_in):
        if _str2.find(str_in[i]) >= 0:
            check_length()
            last_v = ''
        else:
            last_v += str_in[i]
        i += 1
    check_length()
    return res_list

print('using re:', re_filter(_str))
print('not using re:', notRe_filter(_str))

# Задание-2:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

print('Задание 2')
# создание файла
def createFile(file_name):
    numbers = ''
    while len(numbers) < 2500:
        numbers += str(random.randint(0, 9))
    with open(file_name, 'w') as file:
        file.write(numbers)
# поиск самой длинной последовательности в файле
def findnumbers(file_name):
    with open(file_name, 'r') as file:
        line = file.readline()
        max_v = ''
        current_v = ''
        last_v = ''
        check_length = lambda: current_v if len(current_v) > len(max_v) else max_v
        for v in line:
            if v != last_v:
                max_v = check_length()
                current_v = ''
            current_v += v
            last_v = v
        return check_length()

createFile('numbers.txt')
print(findnumbers('numbers.txt'))
