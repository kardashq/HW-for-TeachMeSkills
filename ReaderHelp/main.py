"""Необходимо сделать программу помощник читателя, использовать ООП.
Программа должна принять от пользователя слово или некоторое количество слов,
в ответ программа должна выдать все названия книг в тексте которых есть все
введенные пользователем слова. """


from BooksNames import BooksNames
from finder import Finder


def reader_help():
    """Функция работы проекта"""
    BooksNames.get_filenames()
    Finder.finder()
    if len(Finder.find_result) > 0:
        print("Найдено в: ", end="\n")
        print(*Finder.find_result, sep='\n')
    else:
        print("Ничего не найдено")


if __name__ == "__main__":
    """Запуск проекта"""
    reader_help()
