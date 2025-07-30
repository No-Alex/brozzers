"""
Дано натуральное число
Выведите его последнюю цифру
"""

def get_last_digit(num: int) -> int:
    """
    num: получает через параметр положительное целое (натуральное) число
    Return: возвращает целое однозначное число - последнюю цифру параметра
    """

    return num % 10


if __name__ == '__main__':
    in_number = 148.85
    if in_number > 0:
        if type(in_number) == int:
            print(get_last_digit(in_number))
        else:
            print("Аргумент неверного типа или диапазона!")
