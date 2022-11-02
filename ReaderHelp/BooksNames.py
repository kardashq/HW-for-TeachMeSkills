import os


class BooksNames:
    """Собирает все названия файлов/книг, лежащих в папке 'Books'.
    Должны быть книги в формате .pdf"""
    files: list = []

    @classmethod
    def get_filenames(cls):
        for filename in os.listdir("../Books"):
            cls.files.append(filename)