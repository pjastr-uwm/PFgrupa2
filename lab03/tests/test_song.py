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

    def test_add_artist(self):
        song1 = Song("Bohemian Rhapsody", 355)
        song1.add_artist("Freddie Mercury")
        self.assertIn("Freddie Mercury", song1.artists)
        song1.add_artist("Brain May")
        self.assertIn("Brain May", song1.artists)
        song1.add_artist("Roger Taylor")
        self.assertIn("Roger Taylor", song1.artists)

    def test_add_empty_artist(self):
        song1 = Song("Bohemian Rhapsody", 355)
        with self.assertRaises(ValueError) as context:
            song1.add_artist("")

        self.assertEqual(str(context.exception), "Artist name cannot be empty")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
