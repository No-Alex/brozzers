"""Утилита поиска события в логе.

    - требование 1
    - требование 2
    - требование N

Notes:
    для отладки использовал файл
    https://www.gutenberg.org/cache/epub/12655/pg12655.txt

    концепции:
        - регулярные выражения
        - интерфейс командной строки
        - контекстный менеджер
        - исключения / exceptions
        - тестирование + tdd
        - чтение/запись файлов
        - логирование

    применение
        - re
        - argparse
        - tempfile
        - pathlib
        - doctest
        - pytest
        - logging
"""


import argparse
import re
from pathlib import Path


def get_parameters():
    """Возвращает значения, переданные параметрам утилиты.

    TODO
        - doctest


    """
    parser = argparse.ArgumentParser()
    parser.add_argument('search_pattern')
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    args = parser.parse_args()

    data = {
        'search_pattern': args.search_pattern,
        'input_file': Path(args.input_file),
        'output_file': Path(args.output_file),
    }
    return data


def get_matches(pattern: str, filename: Path) -> str:
    """Построчно читает текстовый файл.

    Возвращает строки, соответствующие шаблону.
    Если совпадений не найдено, возвращает пустой список.

    """
    results: list[str] = []

    with open(filename, 'r', encoding='utf-8') as f:
        # TODO
        # logger.info(f'открыл файл {f}')
        i: int = 1
        for line in f:
            line = line.strip()
            if re.search(pattern, line):
                # TODO
                # logger.info(f'нашел совпадение в строке {i}')
                results.append(line)
            i += 1
    return results

def get_view(data: list[str]):
    """Возвращает представление данных."""
    print(data)


if __name__ == '__main__':
    params = get_parameters()
    pattern_to_search = params['search_pattern']
    file_to_search = params['input_file']
    report_to_write = params['output_file']
    results = get_matches(pattern_to_search, file_to_search)

