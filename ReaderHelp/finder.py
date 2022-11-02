from PyPDF2 import PdfFileReader
from BooksNames import BooksNames


class Finder:
    """Поиск введенных пользователем слов по книгам"""
    find_result: list = []

    @classmethod
    def finder(cls):
        user_input = input('Введите что ищете: ')
        for name in BooksNames.files:
            pdf_document = f"../Books/{name}"
            with open(pdf_document, "rb") as file:
                pdf = PdfFileReader(file, strict=False)
                pages = pdf.getNumPages()
                for i in range(pages):
                    page = pdf.getPage(i)
                    text = page.extractText()
                    if user_input.lower() in text.lower():
                        cls.find_result.append(name)
                        break
