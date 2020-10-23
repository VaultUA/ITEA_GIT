"""
Определить студентов с баллом выше среднего
Пользователь вводит данные о количестве студентов, их фамилии, имена и балл для каждого.
Программа должна определить средний балл и вывести фамилии и имена студентов, чей балл выше среднего.
"""
# test data
# journal = {'name': ['Владимир', 'Евгений', 'Юлия'],
#            'surname': ['Чирковский', 'Задорожний', 'Бондаренко'],
#            'value': ['10', '4', '12']}
# end test

journal = {"name": [],
           "surname": [],
           "value": []}
# определяем количество записей в словарь и циклом вводим все необходимые параметры
a = int(input("Количкство студентов: "))
print("Количество студентов в журнале:", a)
if a == 0:
    print("Опять никто не пришел :( ")
    exit()
else:
    while 0 < a:
        name = input('Введите имя: ')
        journal["name"].append(name)
        surname = input('Введите фамилию: ')
        journal["surname"].append(surname)
        value = int(input('Введите балл: '))
        journal["value"].append(value)
        a -= 1
# Определяем средний балл
average = 0
x = 0
for i in journal['value']:
    x += int(i)
    average = x / len(journal['value'])
print("Средний балл всех студентов:", average)
# Находим студентов с баллом выше среднего
averIndex = []
for i in journal['value']:
    if float(i) > average:
        averIndex += str(journal['value'].index(i))
# Выводим ФИО найденых студентов
print("Список студентов с баллом выше среднего:")
for i in averIndex:
    for key in journal:
        if key != "value":
            print(journal.setdefault(key)[int(i)], end=' ')
    print()
