import unittest
from src.shopping_cart import ShoppingCart


class TestShoppingVart(unittest.TestCase):

    def setUp(self):
        self.empty_card = ShoppingCart([])
        self.card = ShoppingCart(["Apple", "Orange"])

    def test_add_postive(self):
        self.empty_card.add_item("Bread")
        s1 = ShoppingCart(["Bread"])
        self.assertEqual(self.empty_card, s1)

    def test_string_representation(self):
        self.assertEqual(str(self.card), "Shopping card: ['Apple', 'Orange'].")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
