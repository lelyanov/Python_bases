# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <dir_name> - меняет текущую директорию на одну из внутренних
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
# ИСПОЛЬЗОВАТЬ МОДУЛИ SYS, OS, SHUTIL

import os
import sys
import shutil

try:
    key = sys.argv[1]
except IndexError:
    key = None

try:
    arg2 = sys.argv[2]
except IndexError:
    arg2 = None

def help():
    print('===================================================')
    print(f'Текущий каталог: {os.getcwd()}')
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <dir_name> - меняет текущую директорию на одну из внутренних")
    print("ls - отображение полного пути текущей директории")
    print('===================================================')

def cp():
    if not arg2:
        print("Не указано имя файла")
        return
    try:
        shutil.copy2(arg2, f'copy_{arg2}')
        print(f'Файл скопирвоан: {arg2}')
    except Exception:
        print('Ошибка копирования')

def rm():
    if not arg2:
        print("Не указано имя файла")
        return
    req = input(f'Вы действительно хотите удалить файл {arg2}? y/n: ')
    if req == 'n':
        print('Отмена операции')
        return
    elif req != 'y':
        print('Операция не определена')
        return
    try:
        os.remove(arg2)
        print(f'Файл {arg2} удален')
    except Exception:
        print('Ошибка удаления')

def cd():
    if not arg2:
        print("Не указан путь до новой директории")
        return
    try:
        os.chdir(arg2)
        print(os.getcwd())
    except Exception as e:
        print('Ошибка перехода')

def ls():
    print(os.getcwd())

if __name__ == '__main__':
    do = {
        "cp": cp,
        "rm": rm,
        "cd": cd,
        "ls": ls
    }

    if key and do.get(key):
        do[key]()
    else:
        print("Команда не найдена")
        help()