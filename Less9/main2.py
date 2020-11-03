from Student import Student


def readBD(filename: str, bd: list):
    with open(filename) as file:
        for line in file:
            lineList = line.strip().split(' ')

            bd.append(Student(lineList[0].split('=')[1],
                              lineList[1].split('=')[1],
                              lineList[2].split('=')[1],
                              lineList[3].split('=')[1]))


def printBD(bd: list):
    print('%-12s%-12s%-8s%-12s%-15s' % ('Name', 'Surname', 'Class', 'Birthday', 'Age(in day)'))

    for student in bd:
        print('%-12s%-12s%-8s%-12s%-15s' % (student.name_, student.surname_,
                                            student.clas_, student.dob_, student.getAgeinDay()))


if __name__ == '__main__':

    bdStudents = []

    readBD('input.txt', bdStudents)
    # printBD(bdStudents)
    #
    # print()
    # print()
    #
    # bdStudents = sorted(bdStudents)
    # printBD(bdStudents)

    print(str(bdStudents[0]))
