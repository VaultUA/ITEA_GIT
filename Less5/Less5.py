# # import array as ar
# # myArray = ar.array('i', [1, 2, 3, 4, 5])
# # print(myArray)
# # myArray.append(90)
# # print(myArray)
# #
# # for i in myArray:
# #     print(i)
# #
# # myArray.pop()
# # print(myArray)
# #
# # myArray.pop(2)
# # print(myArray)
# # k = myArray.pop(2)
# # print(k)
# # print(myArray)
#
# #
# # myList = []
# # print(type(myList))
# # myList2 = list("Hello World")
# # print(type(myList2))
# #
# #
#
# mylst = []
# for i in range(1,11):
#     if i % 2 == 0:
#         mylst.append(i * 100)
# print(mylst)
#
# mylst2 = [x * 100 for x in range(1, 11) if x % 2 == 0]
# print(mylst2)
#
#
#


a = [2, -3, -5, 3, 5]
minI = 0
for i in range(1, len(a)):
    if abs(a[i]) < abs(a[minI]):
        minI = i
print(minI + 1)
