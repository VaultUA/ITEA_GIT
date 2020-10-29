# def sqare(a):
#     return a ** 2
#
# print(sqare(4))
#
# # lambda
# sqare2 = lambda a: a ** 2
# print(sqare2(4))
#
# #######################
# mass = [2, 18, 9, 22, 17, 24, 8, 12, 27]
# res = []
# for i in mass:
#     if i % 2 == 1:
#         res.append(i)
# print(res)
# ######################
# def test2(x):
#     if x % 2 ==1:
#         return True
#     return False
#
# res2 = filter(test2, mass)
# print(list(res2))
# #####################
#
# res3 = filter(lambda a: a % 2 == 1, mass)
# print(list(res3))
# #######################
#
# res4 = map(lambda a: a * 2, mass)
# print(list(res4))
# print(list(map(str, mass)))
#
# ########################
#
# a = [1, 4, -5, 2, -3, 6]
# print(sorted(a))
# print(sorted(a, key=lambda x: abs(x)))
#
# ####################
# d = {1: "b", 2: "c", 4: "d", 3: "a"}
# print({k: v for k, v in sorted(d.items(), key= lambda x: x[1])})
#
# ########################
#
# f_sorted_dict_byVal = lambda dict: {k: v for k, v in sorted(d.items(), key= lambda x: x[1])}
# print(f_sorted_dict_byVal(d))
#
# f_sorted_dict_byKey = lambda dict: {k: v for k, v in sorted(d.items())}
# print(f_sorted_dict_byKey(d))

####### CLASS

# a = 5
# b = "Hello"
# c = [1, 2, 3]
#
# print(type(a))
# print(type(b))
# print(type(c))
#


# student1 = Student('Volodymyr', 'Chyrkovskyi', '3-b', '08.0.7.1987' )
# student2 = Student('Ivan', 'Programmer', '10-a', '08.0.7.1987')
#
# print(student1.name, '-', student1.clas)
# print(student2.name, '-', student1.clas)
#
# student1.setClass("4-b")
#
# print(student1.name, '-', student1.clas)
# print(student2.name, '-', student1.clas)

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

    ####print(bdStudents[0].getAgeinDay)
    print(sorted(bdStudents, key=lambda stud: getageinday()))
