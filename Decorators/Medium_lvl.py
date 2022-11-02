"""medium lvl: декоратор фильтрующий указаный элемент
Пример:
@my_filter(filt="Oleg")
def a(g,h,j):
    pass

a(1,2,"Oleg") # > Exception"""


def my_filter(filt):
    def decor(func):
        def wrapper(*args):
            if filt in args:
                raise Exception(f'Тут есть {filt}')

        return wrapper

    return decor


@my_filter(filt='Oleg')
def func2(a, b, c):
    pass


func2(1, 2, "Oleg") #test
