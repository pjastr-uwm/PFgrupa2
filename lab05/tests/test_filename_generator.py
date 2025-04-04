import unittest
from unittest.mock import patch
from datetime import datetime
from src.filename_generator import generate_unique_filename


class TestFilenameGeneator(unittest.TestCase):

    @patch("src.filename_generator.datetime")
    def test_format_postive(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024,2,29,10,53, 23)

        result = generate_unique_filename()
        self.assertEqual(result, "file_20240229_105323.txt")