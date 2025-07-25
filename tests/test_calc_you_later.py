import pytest
from utils.calc_you_later import add, mult, main


def test_add() -> int:
    expected = 0
    actual = add(-1, 1)
    assert expected == actual

def test_mult() -> int:
    expected = 0
    actual = mult(0, 1)
    assert expected == actual

def test_main(capsys):
    main(['add', '1', '1', '-v', '2'])
    captured = capsys.readouterr()
    assert captured.out == 'Сумма 1 и 1 равна 2\n'
