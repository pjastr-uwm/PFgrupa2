import pytest
from src.shopping_cart import Product, ShoppingCart

@pytest.fixture
def product():
    return Product(345, "Milk", 3.45)

@pytest.fixture
def empty_cart():
    return ShoppingCart()


def test_adding_correct(empty_cart, product):
    empty_cart.add_product(product, quantity=2)
    assert empty_cart.get_product_count() == 2
    assert product.id in empty_cart.products.keys()
    assert empty_cart.get_total_price() == 6.9

@pytest.mark.parametrize("q", [1,5, 10, 900])
def test_multiple_adding(empty_cart, product, q):
    empty_cart.add_product(product, quantity=q)
    assert empty_cart.get_product_count() == q
