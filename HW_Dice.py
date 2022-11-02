"""
Создать обьект "Игральный кубик" : Атрибуты: к-во граней Методы: бросок
Так же написать ф-цию которая будет бросать выбраные кубики.
"""

from random import randint
import time


class Dice:
    facet = 6

    def throw(self):
        print('Бросоооок!', end=' ')
        time.sleep(1)
        print(f'Выпавшая комбинация: {randint(1, self.facet)} {randint(1, self.facet)}')


dice = Dice()
dice.throw()
