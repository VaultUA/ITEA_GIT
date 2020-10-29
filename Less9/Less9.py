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


















