"""
#Смена переменных местами
start = 1
end = 3
start, end = end, start
"""

#for i in 'Hello World':
#    print(i * 2, end=' ')

#print(*range(2,10))

#for i in range(1, 11):
#    print(i)


#for i in 'Hello World':
#    if i == 'o':
#        continue
#    print(i, end='')

#for i in 'Hello World':
#    if i == 'o':
#        break
#    print(i, end='')


#for x in range(10):
#    for y in range(10):
#        for z in range(10):
#            print(x,y,z)

#count = 30
#cash = 100
#cost_pens = 10
#cost_pencils = 5
#cost_erasers = 2
#for count_pens in range(cash//cost_pens + 1):
#    for count_pencils in range(cash // cost_pencils + 1):
#        for count_erasers in range(cash // cost_erasers + 1):
#            if (cost_pens * count_pens + cost_pencils * count_pencils + cost_erasers * count_erasers == cash) and \
#                    (count_pens + count_pencils + count_erasers == 30):
#                print("Ручки:", count_pens, "Карандаши",count_pencils, "Ластик:", count_erasers)

'''
n = int(input("Число:"))
chet = 0
nechet = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        chet = chet + 1
    elif i % 2 == 1:
        nechet = nechet + 1

print(chet, nechet)
'''
'''
num = int(input())
even = 0
odd = 0

while num > 0:
    if num % 2 ==0:
        even += 1
    else:
        odd += 1
    num = num // 10
print(even, odd)
'''

### СТРОКИ ###

#s = "Hello"
#print(len(s))
#s = "Hello"
#print(s[0])
#
# string = "превед, медвед"
# string = string.replace(" ","")
# string2 = string[::-1]
# if string.lower() == string2.lower():
#    print("перевертыш")
#
# else:
# print("ПРЕВЕД")
#







