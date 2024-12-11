import unittest
from src.utils import generate_random_list

class TestUtils(unittest.TestCase):
    def test_generate_random_list(self):
        result = generate_random_list(5, 10)
        self.assertEqual(len(result), 5)
        self.assertTrue(all(1 <= x < 10 for x in result))
