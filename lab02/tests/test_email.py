import unittest
from src.email import validate_email


class TestEmail(unittest.TestCase):

    def setUp(self):
        pass

    def test_validate_positive(self):
        # self.assertEqual(validate_email("info@onet.pl"), True)
        self.assertTrue(validate_email("info@onet.pl"))

    def test_validate_negative(self):
        self.assertFalse(validate_email("abcXYZ"))

    def test_integer_argument(self):
        with self.assertRaises(TypeError):
            validate_email(567)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
