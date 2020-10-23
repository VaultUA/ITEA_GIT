# #a = input("")
# a = "_as@d"
# if 'a' <= a[0] <= 'z' or a[0] == '_':
#     for i in a:
#         if not ('a' <= i.lower() <= 'z' or '0' <= i <= '9' or i == '_' ):
#             print("no")
#             quit()
#     print("yes")
# else:
#     print("no")


# name = "Vova"
# age = 33
# #print("My name is", name, ". I'm,", age, "old")
# print("My name is %s. I'm %d" % (name, age))
#

## Создание своей функции
# add имя, a,b аргументы
# def add(a, b):
#     c = a + b
#     # указываем, что нужно вернуть с функции
#     return c
#
#     # Вариант 2
#     # def add(a, b):
#     #     return a + b
#
# ####
#
#
# x = 5
# y = 5
# res = add(x, y)
# print(res)

# import random

# print(random.random())
# print(random.randint(1,100))
#
# for i in range(10):
#     print(random.randint(1,10))

# print(random.choice("Hello World"))

#
# import myModule
# print(myModule.add(4, 2, 3))
import math


def circle(a):
    return math.pi * (a ** 2)


def square(a, b):
    return a * b


def triangle(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s


if __name__ == "__main__":
    choice = int(input("Выберите фигуру: Круг: 1 , Прямоугольник: 2, треугольник: 3\n"))
    if choice == 1:
        r = int(input("введите радиус\n"))
        print(circle(r))
    elif choice == 2:
        a = int(input("введите длину стороны А\n"))
        b = int(input("введите длину стороны В\n"))
        print(square(a, b))
    elif choice == 3:
        a = int(input("введите длину стороны А\n"))
        b = int(input("введите длину стороны В\n"))
        c = int(input("введите длину стороны C\n"))
        print(triangle(a, b, c))
    else:
        print("ошибка ввода")
