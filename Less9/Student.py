'''
Объект - Студент
Свойства объекта:
    - Имя
    - Фамилия
    - Класс
    - День рождения
'''

import datetime

class Student:

    def __init__(self, name, surname, clas, dob):

        # Так мы создаем свойства объекта
        self.name_ = name
        self.surname_ = surname
        self.clas_ = clas
        self.dob_ = datetime.date(int(dob.split('.')[2]),
                                  int(dob.split('.')[1]),
                                  int(dob.split('.')[0]))


    def __lt__(self, other):
        return self.dob_ > other.dob_


    def __str__(self):
        return ('name=%s surname=%s class=%s birthday=%s' % (self.name_,
                                                             self.surname_,
                                                             self.clas_,
                                                             self.dob_.strftime('%d.%m.%Y')))


    def getAgeinDay(self):
        return (datetime.datetime.today().date() - self.dob_).days