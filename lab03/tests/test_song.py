import unittest
from src.song import Song

class TestSongInitialization(unittest.TestCase):

    def setUp(self):
        pass

    def test_creation(self):
        song1 = Song("Bohemian Rhapsody", 355)
        self.assertIsInstance(song1, Song)

    def test_initialization(self):
        song1 = Song("Bohemian Rhapsody", 355)
        self.assertEqual(song1.title, "Bohemian Rhapsody")
        self.assertEqual(song1.duration, 355)

    def test_calculate_royalty(self):
        song1 = Song("Bohemian Rhapsody", 355)
        self.assertAlmostEqual(song1.calculate_royalty(), 35.5)
        song2 = Song("Yesterday", 125)
        self.assertAlmostEqual(song2.calculate_royalty(), 12.5)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()