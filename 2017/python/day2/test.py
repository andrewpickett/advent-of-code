import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(18, part_one([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]))
        self.assertEqual(18, part_one(get_data("sample1.txt")))

    def test_part_two(self):
        self.assertEqual(9, part_two([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]))
        self.assertEqual(9, part_two(get_data("sample2.txt")))
