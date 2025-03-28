import unittest
from unittest.mock import Mock, call
from src.data_service import DataService

class TestDataService(unittest.TestCase):

    def setUp(self):
        self.api_mock = Mock()
        self.service = DataService(self.api_mock)

    def test_fetch_user_data_correct_values(self):
        self.api_mock.get_data.side_effect = [{'name': 'Jan'}, {'name': 'Anna'}]

        result = self.service.fetch_user_data(123)
        self.assertEqual(result,{'name': 'Jan'})
        result2 = self.service.fetch_user_data(568)
        self.assertEqual(result2, {'name': 'Anna'})

        self.api_mock.get_data.assert_called()
        self.api_mock.assert_has_calls([
            call.get_data((123,)),
            call.get_data((568,)),
        ])

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()