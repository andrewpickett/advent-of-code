import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(0, part_one(1))
        self.assertEqual(3, part_one(12))
        self.assertEqual(2, part_one(23))
        self.assertEqual(31, part_one(1024))
        self.assertEqual(31, part_one(get_data("sample.txt")))

    def test_part_two(self):
        self.assertEqual(5, part_two(4))
