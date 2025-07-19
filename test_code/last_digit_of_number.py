"""
Дано натуральное число
Выведите его последнюю цифру
"""


def get_last_digit(num: int) -> int:
    """возвращает последнюю цифру числа
    Args:
        num: ожидается положительное целое число
    Returns: возвращает целое однозначное число
    """
    return num % 10


if __name__ == '__main__':
    assert get_last_digit(123) == 3
in_number = 148
if in_number < 0:
    print("Число - не натуральное")
else:
    get_last_digit(in_number)
