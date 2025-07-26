import pytest
from utils.calc_you_later import IntegerCalculator


@pytest.fixture
def calc():
    """Возвращаю инстанс калькулятора."""
    return IntegerCalculator()

def test_add_two_numbers(calc):
    expected = 0
    actual = calc.add(-1, 1)
    assert expected == actual

def test_add_three_numbers(calc):
    expected = 6
    actual = calc.add(1, 2, 3)
    assert expected == actual

def test_add_multiple_numbers(calc):
    expected = 4950
    numbers = range(100)
    actual = calc.add(*numbers)
    assert expected == actual

def test_mult_two_numbers(calc):
    expected = 0
    actual = calc.mult(0, 1)
    assert expected == actual

# def test_main(capsys):
#     main(['add', '1', '1', '-v', '2'])
#     captured = capsys.readouterr()
#     assert captured.out == 'Сумма 1 и 1 равна 2\n'
