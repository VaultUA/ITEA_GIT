# Удаление лишних пробелов
# Вводится ненормированная строка, у которой могут быть пробелы в начале, в конце и между словами более одного пробела.
# Привести ее к нормированному виду, т.е. удалить все пробелы в начале и конце, а между словами оставить только один пробел.
# (подсказка: посмотрите на функцию strip())
import re
a = "   Привет     всем   людям      на  земле!   "
a = a.strip()
a = re.sub(" *\s", " ", a)
print(a)
