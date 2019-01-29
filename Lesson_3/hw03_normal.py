# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
import math

print('Задание 1')

n = int(input('Фибоначчи, начальное положение: '))
m = int(input('Фибоначчи, конечное положение: '))
numbers = []
numbers.append(0) # Добавил 0 позицию, для логичного ввода начальной позиции через input

# 1-1 Вычисление последовательности Фибоначчи через динамическое программирование
def fibonacci_dynamic(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
        numbers.append(a)

fibonacci_dynamic(m)
print('Фибоначчи динамическим программированием: ', numbers[n:])

# 1-2 Вычисление последовательности Фибоначчи через рекурсии (долгое время выполнения на большом диапазоне)
def fibonacci_recursion(n, m):
    def _fibo(m):
        if (m == 1 or m == 2):
            numbers.append(1)
            return 1
        else:
            v = _fibo(m - 1) + _fibo(m - 2)
            numbers.append(v)
            return v
    _fibo(m)
    new_numbers = list(set(numbers))
    new_numbers.append(1)
    return sorted(new_numbers)[n:]

numbers.clear()
numbers.append(0)
print('Фибоначчи через рекурсии: ', fibonacci_recursion(n, m))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print('Задание 2')

# Сортировка пузырьковым методом
def bubble_sort(*args):
    arr = []
    [arr.append(number) for number in args]
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

print('Результат сортировки пузырьком:', bubble_sort(1,5,6,8,43,3,2,87,23,7))

#Задача-3:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

print('Задание 3')

# Функция определение параллелограмма
def is_paralelogram(a,b,c,d):
    # 1. Вычисление длины стороны
    getLength = lambda x1, y1, x2, y2: math.sqrt(((x2 - x1)**2 + (y2 - y1)**2))
    ab = getLength(a.get('x'), a.get('y'), b.get('x'), b.get('y'))
    cd = getLength(c.get('x'), c.get('y'), d.get('x'), d.get('y'))
    ad = getLength(a.get('x'), a.get('y'), d.get('x'), d.get('y'))
    bc = getLength(b.get('x'), b.get('y'), c.get('x'), c.get('y'))
    # 2. Сравнение длин сторон
    return ab == cd and ad == bc

print('Результат определения параллелограмма: ', is_paralelogram({'x': 0, 'y': 0}, {'x': 10, 'y': 0}, {'x': 16, 'y': 5}, {'x': 6, 'y': 5}))