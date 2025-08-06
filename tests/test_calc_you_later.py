import pytest
from utils.calc_you_later import IntegerCalculator, calc_runner, OutOfRangeError


@pytest.fixture
def calc():
    """Возвращаю инстанс калькулятора."""
    return IntegerCalculator()

def test_add_two_numbers(calc):
    assert calc.add(-1, 1) == 0

def test_add_three_numbers(calc):
    assert calc.add(1, 2, 3) == 6

def test_add_multiple_numbers(calc):
    numbers = range(100)
    assert calc.add(*numbers) == 4950

def test_subtract_two_numbers(calc):
    assert calc.sub(10, 7) == 3

def test_mult_two_numbers(calc):
    assert calc.mult(0, 1) == 0

def test_mult_three_numbers(calc):
    assert calc.mult(1, 2, 3) == 6

def test_mult_multiple_numbers(calc):
    nums = [2**i for i in range(0, 8)]
    result = 1
    for num in nums:
        result *= num
    assert result == 268435456

def test_num_is_out_of_range():
    num_1 = -2**16 - 1
    num_2 = 0
    with pytest.raises(OutOfRangeError):
        calc_runner()
