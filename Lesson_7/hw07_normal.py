'''
Задача-1: Создать класс Матрица. В конструктор класса передавать переменную
содержащую матрицу в виде списка списков. В конструкторе класса преобразовать
список списков в привычный матричный вид. Переопределить стандартное поведение
методов __add__ и __str__ класса. Создать два экземпляра класса Матрица с данными.
Метод __add__ должен реализовывать сложение матриц, а __str__ - вывод итоговой
матрицы.
'''

class Matrix:
    def __init__(self, data):
        self.matrix = data
        self.matrix_str = self.getMatrixInStr()     # по условию преобразовать в конструкторе класса

    def getMatrixInStr(self):
        v = ''
        for i in self.matrix:
            v += str(i).replace(',', ' ').replace('[', '|').replace(']', '|') + '\n'
        return v

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix)):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        self.matrix_str = self.getMatrixInStr()

    def __str__(self):
        return self.matrix_str

matrix1 = Matrix([[1, 2, 3], [2, 6, 4], [1, 3, 6]])
matrix2 = Matrix([[3, 6, 1], [3, 3, 4], [5, 1, 2]])

matrix1.__add__(matrix2)
print('Результат сложения матриц: ')
print(matrix1)