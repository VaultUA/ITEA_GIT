'''
num = int(input("Введите число: "))
step = int(input("Введите ножитель: "))

if step < 100:
    print(num ** step)
else:
    print("множитель больше 100")
'''
'''
kop = int(input("Число: "))

if 5<= kop <= 20 or 5<= kop % 10 <= 9 or kop % 10 ==0:
    print(kop, 'копеек')
elif kop % 10 == 1:
    print(kop, 'копейка')
elif 2 <= kop % 10 <= 4:
    print(kop, 'копейки')
'''
'''
try:
    num = int(input(""))
    print("num")

except ValueError:
    print("not number")
'''
'''
from math import sqrt
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
D = b ** 2 - 4 * a * c
if D < 0:
    print("Действительных корней нет")
elif D == 0:
    x = -b / (2 * a)
    print("x =", x)
else:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print("x1 =", x1, "X2 =", x2)
'''
'''
a = int(input("a:"))
b = int(input("b:"))
print(a, "*", b, "=")
z = int(input(""))
if z == a * b:
    print("ответ верный")
else:
    print("Вы ввели неверный ответ. Правильный ответ:", a * b)
'''

i = 0
while i <= 20:
    print(i)
    i += 1