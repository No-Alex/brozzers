"""Предоставляет базовые арифметические операции.

Для выполнения теста используй инструкцию

python arithmetic.py -v
"""

def add(n: int, m: int) -> int:
    """Верни сумму двух целых чисел.

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
    if not isinstance(n, int):
        raise ValueError('число n должно быть представлено типом int')
    if (n < -100) or (n > 100):
        raise OverflowError('число n выходит за пределы допустимого диапазона')
    if not isinstance(m, int):
        raise ValueError('число m должно быть представлено типом int')
    if (m < -100) or (m > 100):
        raise OverflowError('число m выходит за пределы допустимого диапазона')
    return n + m


def mult(n: int, m: int) -> int:
    """Верни произведение двух целых чисел.

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
    # TODO
    raise NotImplementedError('функция не определена')


if __name__ == '__main__':
    import doctest
    doctest.testmod()

