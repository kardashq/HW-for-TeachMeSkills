"""
hard: кеширующий декоратор
"""

def cashe_func(func):
    cache_dictionary = {}

    def wrapper(*args):
        if args in cache_dictionary.keys():
            print("result from cache: ", end='')
            return cache_dictionary[args]
        print("result: ", end='')
        cache_dictionary[args] = func(*args)
        return cache_dictionary[args]

    return wrapper


@cashe_func
def f(a, b, c):
    return a * b * c


# tests
print(f(1, 2, 3))
print(f(1, 2, 3))
print(f(2, 2, 3))
print(f(2, 2, 3))
