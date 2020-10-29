'''
Объект - студент
Свойства объекта:
    - имя
    - фамилия
    - класс
    - др
'''
import datetime


class Student:

    def __init__(self, name, surname, clas, dob):
        # Создаем свойства объекта
        self.name = name
        self.surname = surname
        self.clas = clas
        self.dob = dob

    # def setClass(self,newClass):
    #     self.clas = newClass

    def getageinday(self):
        tDOB = datetime.date(int(self.dob.split('.')[2]),
                             int(self.dob.split('.')[1]),
                             int(self.dob.split('.')[0]))

        taday = datetime.datetime.today().date()

        return (today - tDOB).days
