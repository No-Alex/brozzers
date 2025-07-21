""" Программа получает на вход через запятую два целых числа number_1 и number_2
    При этом number_1 может быть меньше number_2, а может быть больше.
    Создайте диапазон чисел с шагом 1 в обратном порядке
    от наибольшего числа к наименьшему (включительно).
    Выведите результат через запятую.
    Sample Input 1:
    0, 10
    Sample Output 1:
    10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0
    Sample Input 2:
    22, 15
    Sample Output 2:
    22, 21, 20, 19, 18, 17, 16, 15
"""


def create_range_decr_2_int(num_max, num_min):
    """
    На вход функция получает два целых числа
    Первое заведомо больше второго
    Формирует диапазон чисел с шагом 1 в обратном порядке
    от наибольшего числа к наименьшему (включительно).
    Выводит результат через запятую.
    """
    return list(range(num_max, num_min - 1, -1))


def main():
    startstop = "7, 9"
    start, stop = list(map(int, startstop.split(", ")))
    if stop > start:
        stop, start = start, stop
    assert create_range_decr_2_int(start, stop) == [9, 8, 7]
    assert create_range_decr_2_int(start, stop) == [9, 8, 6], "Wrong result"

if __name__ == "__main__":
    main()
