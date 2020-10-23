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


def writeMass(mass, N, fileName):
    with open(fileName, 'w') as file:
        for i in range(N):
            for j in range(N):
                file.write("%-4d" % mass[i][j])
            file.write('\n')


# i + j = n - 1
# j = n - 1 - i
def exchange(mass, N):
    for i in range(N):
        for j in range(N):
            if i == j:
                mass[i][j], mass[i][N - 1 - i] = mass[i][N - 1 - i], mass[i][j]


if __name__ == '__main__':
    mass, N = readMass(r'matrix.txt')

    printMass(mass, N)

    print()

    exchange(mass, N)

    printMass(mass, N)
    writeMass(mass, N, r'output.txt')
