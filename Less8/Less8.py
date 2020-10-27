# def less(arg1: dict, arg2: dict) -> bool:
#     b1 = arg1['birthday'].split('.')
#     b2 = arg2['birthday'].split('.')
#
#     if int(b1[2]) > int(b2[2]):
#         return True
#     elif (int(b1[2]) == int(b2[2])) and (int(b1[1]) > int(b2[1])):
#         return True
#     elif (int(b1[2]) == int(b2[2])) and (int(b1[1]) == int(b2[1])) and (int(b1[0]) > int(b2[0])):
#         return True
#     return False
#
#
# def more(arg1: dict, arg2: dict) -> bool:
#     b1 = arg1['birthday'].split('.')
#     b2 = arg2['birthday'].split('.')
#
#     if int(b1[2]) < int(b2[2]):
#         return True
#     elif (int(b1[2]) == int(b2[2])) and (int(b1[1]) < int(b2[1])):
#         return True
#     elif (int(b1[2]) == int(b2[2])) and (int(b1[1]) == int(b2[1])) and (int(b1[0]) < int(b2[0])):
#         return True
#
#     return False
#
#
# def readfile(filename: str) -> list:
#     userBD = []
#
#     for line in open(filename):
#         user = {}
#
#         for j in line.split():
#             user[j.split('=')[0]] = j.split('=')[1]
#
#         userBD.append(user)
#
#     return userBD
#
#
# def printDB(d: list):
#     print("%-12s%-12s%-6s%-12s" % ('Name', 'Surname', 'Class', 'Birthday'))
#
#     for userDic in d:
#         print("%-12s%-12s%-6s%-12s" % (userDic['name'], userDic['surname'], userDic['class'], userDic['birthday']))
#
#
# if __name__ == '__main__':
#     bd = readfile("input.txt")
#     #printDB(bd)
#
#     oldStudent = bd[0]
#     youngStudent = bd[0]
#
#     for user in bd:
#         if more(user, oldStudent):
#             oldStudent = user
#
#         if less(user, youngStudent):
#             youngStudent = user
#
#     print("\nСамый старший:")
#     print("%-12s%-12s%-6s%-12s" % ('Имя', 'Фамилм', 'Клас', 'Д.Р.'))
#     print("%-12s%-12s%-6s%-12s" % (youngStudent['name'], youngStudent['surname'], youngStudent['class'], youngStudent['birthday']))
#
#     print("\nСамый младший:")
#     print("%-12s%-12s%-6s%-12s" % ('Имя', 'Фамилм', 'Клас', 'Д.Р.'))
#     print("%-12s%-12s%-6s%-12s" % (oldStudent['name'], oldStudent['surname'], oldStudent['class'], oldStudent['birthday']))
#################################################


"""
функциональное программирование
"""















