# Количество слов в строке
# Вводится строка, состоящая из слов, разделенных пробелами. Требуется посчитать количество слов в ней.
import re
a = "Какой солнечный день за окном, пойду гулять!"
b = re.split(' ', a)
print(len(b))