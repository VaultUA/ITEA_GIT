'''
Найти столбец матрицы с максимальной суммой элементов

Задана матрица неотрицательных чисел. Посчитать сумму элементов в каждом столбце. Определить, какой столбец содержит максимальную сумму.

  62   8  19  98  69  81  25  21  98  99
  55  96  67  69  81  43  89  39  22   4
  10  96  98  81  35  34  42  53  41  83
  22  11  55  10  81  36  98  41  96  30
  11  59  49  47  80  83  63  27  79  28
  23  83  85  35  24  80  53  62  17  90
  56  54  53   7  12  63  83  22  23  23
  87  93   5   7  91  63  90  28  37  45
  57  53   5  93  90   1  75   7   3   0
  85  65  15  71  78  90  46  17  98  40
  --  --  --  --  --  --  --  --  --  --
 468 618 451 518 641 574 664 317 514 442

7
'''

import re

def readfile(fileName):
    with open(fileName) as file:
        print(file.read())


def convert(fileName):
    with open(fileName) as file:
        matrix = []
        a = 0
        for row in file:
            z = []
            rowStr = row.strip('\n')
            rowStr = re.split(' +', rowStr)
            for i in rowStr:
                z.append(int(i))
            matrix.append(z)
            a += 1
    return matrix, a

def total(matrix, a):
    c = []
    for i in range(a):
        z = 0
        for j in range(a):
            z += int(matrix[j][i])
        c += [z]
        print(z, end=" ")
    return c


def max_num(c):
    maxN = 0
    for i in range(len(c)):
        if c[i] > c[maxN]:
            maxN = i
            maxNi = i
    maxN = c[maxN]
    print()
    return maxN, maxNi


if __name__ == '__main__':

        matrix, a = convert("DZ6.2.txt")
        readfile("DZ6.2.txt")
        print("%-4s" % ('--') * 10)
        c = total(matrix, a)
        maxN, maxNi = max_num(c)
        print("Максимальная сумма", maxN, "в колонке", maxNi + 1)