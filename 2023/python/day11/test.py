import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(True, part_one(""))

    def test_part_two(self):
        self.assertEqual(True, part_two(""))
