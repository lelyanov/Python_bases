
__author__ = 'Лелянов Иван Александрович'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
# с помощью числа определяем ширину поля слева

print('Задача 1')
fruits = ['apple', 'banana', 'lime', 'grapefruit', 'mango']
maxlen = max(map(len, fruits))
[print('{index}. {fruit:>{len}}'.format(index=i+1, fruit=fruit, len=maxlen)) for i, fruit in enumerate(fruits)]

print('\n', 'На случай, если я сделал так, как не должен был еще знать')
i = 1
for fruit in fruits:
    print('{}. {:>{}}'.format(i, fruit, maxlen))
    i += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print('Задача 2')
fruits_1 = ['apple', 'banana', 'lime', 'grapes', 'grapefruit', 'mango', 'pear']
fruits_2 = ['peach', 'apple', 'kiwi', 'banana', 'lime', 'grapefruit', 'persimmon', 'mango', 'tangerine']
i = 0
while i < len(fruits_1):
    if fruits_1[i] in fruits_2:
        fruits_1.remove(fruits_1[i])
    else:
        i += 1
print(fruits_1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print('Задача 3')
numbers = input('Введите числа через пробел: ').split(' ')
numbers = [int(number) for number in numbers]
newlist = []
for number in numbers:
    if number%2 == 0:
        newlist.append(number/4)
    else:
        newlist.append(number*2)
print(newlist)