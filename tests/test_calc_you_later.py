import pytest
from utils.calc_you_later import add, mult


def test_add() -> int:
    expected = 0
    actual = add(-1, 1)
    assert expected == actual

def test_mult() -> int:
    expected = 0
    actual = mult(0, 1)
    assert expected == actual

def test_get_parameters():
    assert 0
