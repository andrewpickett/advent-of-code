import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(32000000, part_one(get_data("sample.txt")))
        self.assertEqual(11687500, part_one(get_data("sample2.txt")))

    def test_part_two(self):
        self.assertEqual(2, part_two(get_data("sample2.txt")))
