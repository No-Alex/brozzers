"""калькулятор для работы с целыми числами

Notes:
    - cli
    - работа только с целыми числами для сохранения точности расчета
    - принимаемые и возвращаемые значения - в диапазоне [-2**31; 2**31-1]
    - арифметические операции
    - сумма и произведение принимают неограниченного количество параметров
    - передача делению знаменателя == 0 поднимает ValueError

    Базовые операции:
        - сложение: add
        - произведение: mult
        - вычитание: sub
        - деление: div

Examples:
    Запуск doctest средствами pytest
    pytest --doctest-modules path/to/test_module.py
"""
import argparse
import sys


class IntegerCalculator:
    pass

    def add(self, *args) -> int:
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
        return sum(args)


    def mult(self, n: int, m: int) -> int:
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
        return 0


def get_operator_and_values(args=None):
    """Получи три параметра командной строки.

    Оператор и два числа

    >>> get_operator_and_values()

    >>> get_operator_and_values()
    Traceback (most recent call last):
        ...
    ArgumentError

    >>> 

    """
    parser = argparse.ArgumentParser()
    parser.add_argument('operation',
                        type=str,
                        choices=['add', 'mult', 'sub', 'div'],
                        help='оператор')
    parser.add_argument('num_1', type=int, help='первое число')
    parser.add_argument('num_2', type=int, help='второе число')

    parser.add_argument('-v', '--verbose',
                        type=int,
                        choices=[0, 1, 2],
                        help='сделать сообщение подробнее')

    args = parser.parse_args(args)

    # TODO
    # if args.verbose:
    #     logger.debug(f'Запрошен подробный вывод уровня {args.verbose}')

    return {
        'operation': args.operation,
        'num_1': args.num_1,
        'num_2': args.num_2,
        'verbose': args.verbose,
    }


def main(args=None):
    user_input = get_operator_and_values(args)
    verbose = user_input['verbose']
    operation = user_input['operation']
    num_1 = user_input['num_1']
    num_2 = user_input['num_2']
    if operation == 'add':
        if verbose == 2:
            print(f'Сумма {num_1} и {num_2} равна {add(num_1, num_2)}')
        elif verbose == 1:
            print(f'{num_1} + {num_2} = {add(num_1, num_2)}')
        else:
            print(add(num_1, num_2))


if __name__ == '__main__':
    sys.exit(main())

