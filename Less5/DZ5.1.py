"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random
MyList = [random.randint(1, 100) for i in range(10)]
print("Рандомная одномерная матрица:\n", MyList, "\n")
total = 0
minN = 0
maxN = 0
# поиск минимального занчения
for i in range(1, len(MyList)):
    if MyList[i] < MyList[minN]:
        minN = i
minN = MyList[minN]
print("Минимальное значение: ", minN)
# поиск максимального значения
for i in range(1, len(MyList)):
    if MyList[i] > MyList[maxN]:
        maxN = i
maxN = MyList[maxN]
print("Максимальное значение: ", maxN)
print()
# удаляем с массива минимальное и максимальное значения
for i in MyList:
    if minN == i or maxN == i:
        MyList.remove(i)
for i in MyList:
    total += i
print("Сумма элементов массива без мин и макс значений равна:", total)
