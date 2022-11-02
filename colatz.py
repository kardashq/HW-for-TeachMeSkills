"""
Самая длинная последовательность Коллатца
Следующая итерационная последовательность определена для набора натуральных чисел:
Если n чётное n = n/2 Если n нечётное n = n*3 + 1
Используя приведенное выше правило и начиная с 13, мы генерируем следующую последовательность:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
Видно, что эта последовательность (начиная с 13 и заканчивая 1) содержит 10 терминов.
Хотя это еще не доказано (задача Коллатца), считается, что все стартовые номера заканчиваются на 1.
Какое начальное число, меньшее миллиона, дает самую длинную цепочку?
ПРИМЕЧАНИЕ: Как только цепочка начинается, термины могут превышать один миллион.
Необходимо сделать максимально быстро
#Результат ~1.5-2.0 сек.
"""

import time


def timer(f):
    """ Декоратор подсчета времени"""

    def wrapper():
        st = time.time()
        f()
        et = time.time()
        print(f'Время выполнения {et - st}')
    return wrapper


@timer
def colatz():
    desired_number = 0
    results_dictionary = {}  # Пустой словарь для записи результатов
    for num in range(1, 1000000):
        counter = 0
        temp_num = num
        while temp_num != 1:
            if temp_num % 2 == 0:
                temp_num = temp_num // 2
                if temp_num in results_dictionary.keys():  # Проверка промежуточного результата вычисления на
                    # нахождение его в словаре
                    counter += results_dictionary[temp_num]  # Если есть - просто к счетчику добавляем уже имеющееся
                    # количество шагов для привода к 1
                    temp_num = 1  # Приводим к 1 жестко, чтобы дальше не считать
            else:
                temp_num = temp_num * 3 + 1
                if temp_num in results_dictionary.keys():
                    counter += results_dictionary[temp_num]
                    temp_num = 1
            counter += 1
        results_dictionary[num] = counter  # Записываем в словарь: ключ(число) - значение(кол-во шагов)
    max_count = max(results_dictionary.values())  # Ищем максимальное значение шагов в словаре и записываем в переменную
    for key, value in results_dictionary.items():  # Возвращаем ключ по макс значению
        if value == max_count:
            desired_number = key  # Искомое число
    print(f'Количество шагов: {max_count}\nЧисло:{desired_number}')


colatz()
