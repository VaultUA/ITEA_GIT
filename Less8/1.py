import math


def dialog(func):
    def wrapper():
        int(input("Введите первую величину\n"))
        return wrapper

def radius_square(a):
    return a ** 2

def print_res(func, a):
    return func(a)

choice = int(input("Выберите фигуру: Круг: 1 , Прямоугольник: 2, треугольник: 3\n"))
if choice == 1:
    a = dialog('')
    circle = lambda a: math.pi * (print_res(radius_square, a))
    print(circle(a))
elif choice == 2:
    @dialog
    def dialog2(dialog):
        b = int(input("Введите вторую величину\n"))
        return b
    square = lambda a, b: a * b
    print(square(a, b))