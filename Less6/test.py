# import re
# dz62 = open('dz6.2.txt')
# matrix = dz62.read()
# matrix = matrix.strip(' ')
# matrix = re.split(' +', matrix)
# matrix = matrix.split('\n')
# #matrix = matrix.split('\n')
#
#
# print(matrix)
#

#
# dz62 = open("dz6.2.txt")
# for row in dz62:
#     rowStr = row.strip(' ')
#     rowStr = re.split(' +', rowStr)
#     for i in range(len(rowStr)):
#         print(rowStr[i][0])

import re
with open("dz6.2.txt", 'r') as dz62:
    rowCount = 0
    text = []
    for row in dz62:
        rowStr = row.strip(' ')
        rowStr = re.split(' +', rowStr)
        text.append(rowStr)
        print(text)
        rowCount = (len(rowStr))
    lineCount = 0
    for line in rowStr:
        lineCount += 1
    for i in range(rowCount):
        print(" --", end='',)
    print()
    for i in range(lineCount):
        a = 0
        while a <= int(lineCount):
            print(text[a])
            a += 1



        # for i in range(0, rowCount + 1):
        #     b = []
        #     print(rowStr[i])
        # print()
        # for j in range(0, lineCount + 1):
        #     print(rowStr[j][i])
        #     b += rowStr[j][i]
        #print("%3d" % b, end='')
    #print()
# import re
# matrix = open("dz6.2.txt").read()
# data = matrix.strip("\n")
# print(data.)