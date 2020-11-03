from Student import Student


def readBD(filename: str, bd: list):
    with open(filename) as file:
        for line in file:
            linelist = line.strip().split(' ')

            bd.append(Student(linelist[0].split('=')[1],
                              linelist[1].split('=')[1],
                              linelist[2].split('=')[1],
                              linelist[3].split('=')[1]))


def printBD(bd: list):
    print('%-12s%-12s%-8s%-12s' % ('Name', 'Surname', 'Class', 'Birthday'))

    for student in bd:
        print('%-12s%-12s%-8s%-12s' % (student.name, student.surname, student.clas, student.dob))


if __name__ == "__main__":
    bdStudents = []
    readBD("input.txt", bdStudents)
    printBD(bdStudents)

    # print(bdStudents[0].getAgeinDay)

    print(sorted(bdStudents, key=lambda stud: Student.getageinday(stud)))
