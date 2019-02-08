'''
Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
'''
import math

# Класс треугольника
class Triangle:
    def __init__(self, a, b, c):
        self.ab = self.getLength(a.get('x'), a.get('y'), b.get('x'), b.get('y'))
        self.ac = self.getLength(a.get('x'), a.get('y'), c.get('x'), c.get('y'))
        self.bc = self.getLength(b.get('x'), b.get('y'), c.get('x'), c.get('y'))

    def getArea(self):
        pass
        half_p = (self.ab + self.ac + self.bc) / 2
        return math.sqrt(half_p * (half_p - self.ab) * (half_p - self.ac) * (half_p - self.bc))

    def getHeight(self):
        height_ab = 2 * (self.getArea() / self.ab)
        height_ac = 2 * (self.getArea() / self.ac)
        height_bc = 2 * (self.getArea() / self.bc)
        return {'h_ab': height_ab, 'h_ac': height_ac, 'h_bc': height_bc}

    def getPerimeter(self):
        return self.ab + self.ac + self.bc

    def getLength(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

triangle = Triangle({'x': 1, 'y': 1}, {'x': -2, 'y': 4}, {'x': -2, 'y': -2})

print('S =',triangle.getArea())
print('h {ab, ac, bc} =', triangle.getHeight())
print('P =', triangle.getPerimeter())
