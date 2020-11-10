# from math import pi
# from math import sqrt
#
#
# class Figure:
#     def __init__(self):
#         pass
#
#     def getsquare(self):
#         raise exception("Ошибка! Это общая ф-ия.\nОна не должна вызываться")
#
#
# class Triangle(Figure):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.type = 'Trinagle'
#
#     def getsquare(self):
#         p = (self.a + self.b + self.c) / 2
#         return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
#
#
# class Rect:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         self.type = 'Rect'
#
#     def getsquare(self):
#         return self.a * self.b
#
#
# class Circle:
#     def __init__(self, r):
#         self.r = r
#         self.type = 'Circle'
#
#     def getsquare(self):
#         return self.r ** 2 * pi
#
#
# typeFig = input("Введите тип фигуры (trinagle, rect, circle)")
# figure = None
# if typeFig == 'circle':
#     r = input("Введите радиус")
#     figure = Circle(r)
#
# if typeFig == 'rect':
#     a = input("Введите a")
#     b = input("Введите b")
#     figure = Rect(a, b)
#
# if typeFig == 'trinagle':
#     a = input("Введите a")
#     b = input("Введите b")
#     c = input("Введите c")
#     figure = Triangle(a, b, c)
#
#     print(Figure.getsquare())
#
#
#     dict.get()


#########################


