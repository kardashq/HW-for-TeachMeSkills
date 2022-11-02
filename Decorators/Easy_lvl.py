"""easy lvl: декоратор разворачивающий аргументы
Пример:a(1,2,3) # > a(3,2,1)"""


def revers(func):
    def wrapper(*args):
        print(*args[::-1])

    return wrapper


@revers
def f1(*args):
    print(*args)


f1(5, 4, 3, 2, 1) #test
