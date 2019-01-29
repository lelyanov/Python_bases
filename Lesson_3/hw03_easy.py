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
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

print('Задание 2')

# Функция проверки счастливого билета (решил не ограничивать по количеству символов)
def checkTicket(numbers):
    if len(numbers) == 0: return False
    my_sum = lambda numbers: sum(int(n) for n in numbers)
    _len = int(len(numbers)/2)
    return my_sum(numbers[:_len]) == my_sum(numbers[_len:])

print('Результат определения счастливого билета: ', checkTicket(input('Введите номер билета: ')))

