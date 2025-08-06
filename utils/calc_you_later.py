"""Калькулятор для работы с целыми числами

Notes:
    - принимаемые значения - целые числа в диапазоне [-2**16; 2**16-1]
      - выход за допустимый диапазон поднимает OutOfRangeError
    - операции
      - сложение: add
        - принимает неограниченное количество параметров
      - произведение: mult
        - принимает неограниченное количество параметров
      - вычитание: sub
        - принимает два параметра
      - деление: div
        - принимает два параметра
        - передача делению знаменателя == 0 поднимает ValueError

"""
import argparse
import sys
from functools import reduce


class IntegerCalculator:
    def add(self, *args) -> int:
        """Верни сумму целых чисел.

        >>> add(0, 1)
        1

        >>> [add(i - 1, i) for i in range(1, 7)]  # [0 + 1, 1 + 2, 2 + 3, ...]
        [1, 3, 5, 7, 9, 11]

        >>> add(0, 1.23)
        Traceback (most recent call last):
            ...
        ValueError: число m должно быть представлено типом int

        >>> add(101, -1)
        Traceback (most recent call last):
            ...
        OverflowError: число n выходит за пределы допустимого диапазона
        """
        return sum(args)

    def sub(self, n: int, m: int) -> int:
        """Верни разность двух целых чисел.

        """
        return n - m

    def mult(self, *args) -> int:
        """Верни произведение целых чисел.

        >>> mult(0, 1)
        1

        >>> [mult(i - 1, i) for i in range(1, 7)]  # [0 * 1, 1 * 2, 2 * 3, ...]
        [0, 2, 6, 12, 20, 30]

        >>> mult(-99.9, 23)
        Traceback (most recent call last):
            ...
        ValueError: число m должно быть представлено типом int

        >>> mult(101, -10)
        Traceback (most recent call last):
            ...
        OverflowError: число n выходит за пределы допустимого диапазона
        """
        return reduce(lambda x, y: x*y, args)



class Error(BaseException):
    pass

class OutOfRangeError(Error):
    def __init__(self, message: str):
        self.message = message

def verify_range(*args):
    """Проверяю вхождение переданных значений в ожидаемый интервал."""
    for num in args:
        if num < -2**16 or num > (2**16 - 1):
            raise OutOfRangeError(f'Число {num} находится вне допустимого диапазона')


def calc_runner():
    some_input = (-2**16 - 1, 0)

