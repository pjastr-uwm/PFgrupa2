import pytest
from src.shopping_cart import Product, ShoppingCart


@pytest.fixture
def product():
    return Product(345, "Milk", 3.45)

@pytest.fixture
def product2():
    return Product(444, "Apple", 22.9)

@pytest.fixture
def product3():
    return Product(34454, "Orange", 3.9)

@pytest.fixture
def empty_cart():
    return ShoppingCart()

@pytest.fixture
def filled_cart(empty_cart, product, product2, product3):
    empty_cart.add_product(product, 7)
    empty_cart.add_product(product2, 6)
    empty_cart.add_product(product3, 2)
    return empty_cart

def test_adding_correct(empty_cart, product):
    empty_cart.add_product(product, quantity=2)
    assert empty_cart.get_product_count() == 2
    assert product.id in empty_cart.products.keys()
    assert empty_cart.get_total_price() == 6.9


@pytest.mark.parametrize("q", [1,5, 10, 900])
def test_multiple_adding(empty_cart, product, q):
    empty_cart.add_product(product, quantity=q)
    assert empty_cart.get_product_count() == q

def test_removing_correct(filled_cart, product, product2):
    filled_cart.remove_product(product.id)
    assert filled_cart.get_product_count() == 14
    filled_cart.remove_product(product2.id, 5)
    assert filled_cart.get_product_count() == 9
    assert filled_cart.products[product2.id]["quantity"] == 1

def test_cart_clear(filled_cart, product, product2, product3):
    filled_cart.remove_product(product.id, 7)
    filled_cart.remove_product(product2.id, 6)
    filled_cart.remove_product(product3.id, 2)
    assert filled_cart.get_product_count() == 0
    assert filled_cart.get_total_price() == 0


def test_invalid_removing(filled_cart, product):
    filled_cart.remove_product(product.id, 10)
    assert product.id not in filled_cart.products.keys()