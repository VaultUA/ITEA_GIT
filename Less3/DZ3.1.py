# Самое длинное слово в строке
# Вводится строка слов, разделенных пробелами. Найти самое длинное слово и вывести его на экран.
# Случай, когда самых длинных слов может быть несколько, не обрабатывать.

import re
#a = input("")
a = "Kyiv,is,a,capital,of,Ukraine"
wrd = re.split(',', a)
b = []
c = ""
for i in wrd:
    b.append(len(i))
max_val = sorted(b)[-1]
count = len(re.split(',', a))
for i in range(0, count):
    if len(wrd[i]) == max_val:
        c += (wrd[i]) + " "
print("Самое длинное слово(а): ", c)