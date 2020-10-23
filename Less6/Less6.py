# my_file = open(r"C:\Users\chirkovskiy\Desktop\regexp.pdf")
# print(my_file.name)
# print(my_file.mode)
# print(my_file.closed)
# my_file.close()
# print(my_file.closed)

# my_file = open("test.txt")
# data = my_file.read()
# print(data)
# my_file.close()
# data = my_file.readline()
# print(data)
# data = my_file.readline()
# print(data)
# data = my_file.readlines()
# print(data)
# data = my_file.read(2)
# print(data)

# my_file = open("test.txt", 'w')
#####
# d = ['Hello', 'World']
# my_file.writelines(d)
#####
#####
# my_file.write("testetstetsete")
####

#
# with open("test.txt", 'r') as my_file:
#     for line in my_file:
#         print(line)
#
# print(my_file.closed)
#
#
#

#
# with open("test.txt", 'r') as my_file:
#     for line in my_file:
#         all = line.strip("\n")
#         ru = all.split("-")[0]
#         ect = all.split("-")[1:]
#         for e in ect:
#             lst = e.split(",")
#             for s in range(len(lst)):
#                 print(lst[s], "-", ru)
# saveFile = open("test2.txt", 'w')
# saveFile.write(newDict)


# print(ru)
# print(en)


import re


def readMass(fileName):
    with open(fileName) as file:
        mass = []
        N = 0
        for row in file:
            z = []
            rowStr = row.strip('\n')
            rowStr = re.split(' +', rowStr)
            for i in rowStr:
                z.append(int(i))
            mass.append(z)
            N += 1
    return mass, N


def printMass(mass, N):
    for i in range(N):
        for j in range(N):
            print("%-4d" % mass[i][j], end='')
        print()


def exch(mass, N):
    for i in range(N):
        for j in range(N):
            if i == j:
                mass[i][j], mass[i][N - 1 - i] = mass[i][N - 1 - i], mass[i][j]

if __name__ == "__main__":
    mass, N = readMass(r'matrix.txt')

    printMass(mass, N)
    exch(mass, N)
