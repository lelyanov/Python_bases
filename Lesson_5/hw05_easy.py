# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

# Создание папки
def create_dir(filename):
    try:
        os.mkdir(filename)
        return False
    except:
        return True

# Удаление папки
def remove_dir(filename):
    try:
        os.rmdir(filename)
        return False
    except:
        return True

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
#ТОЛЬКО ПАПКИ, А НЕ ФАЙЛЫ!

# Получить список папок текущей директории
def get_dirs():
    return list(filter(lambda x: os.path.isdir(x), os.listdir(".")))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# ИСПОЛЬЗОВАТЬ ТОЛЬКО МОДУЛЬ OS

# Создать копию скрипта
def create_copy(original, newname):
    with open(original, 'r') as src, open(newname, 'w') as dst:
        dst.write(src.read())

# Вызов функций
if __name__ == '__main__':
    [create_dir(f"dir_{i}") for i in range(1, 10)]
    [remove_dir(f"dir_{i}") for i in range(1, 10)]
    print(get_dirs())
    create_copy(os.path.basename(__file__), f'{os.path.basename(__file__)[:-3]}_copy.py')
