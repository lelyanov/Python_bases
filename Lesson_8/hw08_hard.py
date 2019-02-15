"""
Задание_1. Создайте свое исключение для проверки вводимого числа.
Исключение должно возбуждаться, если пользователь ввел отрицательное число.
Также предусмотрите тот, случай, что пользователь ввел не число, а строку
(здесь можно применить встроенное исключение).
"""


class NegativeNumber(Exception):
    def __str__(self):
        return 'Введенное значение не является положительным'


def check_number(v):
    try:
        v = int(v)
    except ValueError as Err:
        return Err

    try:
        if int(v) < 0:
            raise NegativeNumber
    except NegativeNumber as Err:
        return Err

    return None


err = check_number(input('Введите положительное число: '))
print(err if err is not None else 'Вы справились!')
