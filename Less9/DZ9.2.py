'''
2. Описать класс «домашняя библиотека». Предусмотреть возможность работы с произвольным числом книг,
поиска книги по какому-либо признаку (например, по автору или по году издания), добавления книг в библиотеку,
удаления книг из нее, сортировки книг по разным полям.
'''


# Объявляем свой клас "библиотека"
class library:

    # Задаем свойства класа
    def __init__(self, name, author, year, genre):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre


def open_library():
    if not library:
        a = int(input("Книжная полка пустая\nХотите ее наполнить? (1 - Да, 2 - Нет)\n"))
        if a == 2:
            open_library()
        elif a == 1:
            name = input("Название:\n")
            author = input("Автор:\n")
            year = input("Год:\n")
            genre = input("Жанр:\n")
            add_book(name, author, year, genre)
        else:
            print("Ошибочный ввод")
            open_library()
    else:
        print(library)


def add_book(name, author, year, genre):
    library.append(library(name=name,
                            author=author,
                            year=year,
                            genre=genre))


if __name__ == '__main__':
library = library(\)

open_library()
print(library)
