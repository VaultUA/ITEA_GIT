
import math
def radius_square(a):
    return a * a

def print_res(func, a):
    return func(a)


choice = int(input("Выберите фигуру: Круг: 1 , Прямоугольник: 2, треугольник: 3\n"))
if choice == 1:
   r = int(input("введите радиус\n"))
   circle = lambda r: math.pi * (print_res(radius_square,r))
   print(circle(r))