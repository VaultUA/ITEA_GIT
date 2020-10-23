'''
Пользователь задает кол-во гривен (0 -> 999)
Пользователь задает кол-во копеек (0 -> 99)
Вывести на экран правильную надпись.
Пример:
1, 85 	– 1 гривна, 85 копеек
568, 20	– 568 гривен, 20 копеек
0, 24	– 24 копейки
173, 0	– 173 гривны
0,0 – у вас нет денег =(
'''

grn = int(input("Гривны: \n"))
kop = int(input("Копейки: \n"))
if 0 < grn > 999 or 0 < kop > 99:
    print("Значения вне диапазона \n ГРН: 0-999 \n КОП: 0-99")
    exit()
else:
    if grn == 0 and kop == 0:
        print("Привет, нищеброд")
    elif grn == 0:
        grn = ""
        grnName = ""
    elif grn == 1 or grn % 10 == 1 and grn != 11 and grn % 100 != 11:
        grnName = "гривна"
    elif 2 <= grn <= 4 or 2 <= grn % 10 <= 4:
        grnName = "гривны"
    elif grn >= 5 or grn % 10 >= 5:
        grnName = "гривен"
if kop == 0:
    kop = ""
    kopName = ""
elif 5 <= kop <= 20 or 5 <= kop % 10 <= 9 or kop % 10 == 0:
    kopName = "копеек"
elif kop % 10 == 1:
    kopName = "копейка"
elif 2 <= kop % 10 <= 4:
    kopName = "копейки"

print(grn, grnName, kop, kopName)