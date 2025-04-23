import pytest
from src.discount import calculate_discounted_price


def test_calculate_correct():
    assert calculate_discounted_price(100, 30) == 70


def test_calculate_negative():
    assert calculate_discounted_price(100, 30) != 90


def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_discounted_price(34, "45")