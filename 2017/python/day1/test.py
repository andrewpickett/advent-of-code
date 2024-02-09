import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(3, part_one("1122"))
        self.assertEqual(4, part_one("1111"))
        self.assertEqual(0, part_one("1234"))
        self.assertEqual(9, part_one("91212129"))
        self.assertEqual(9, part_one(get_data("sample.txt")))

    def test_part_two(self):
        self.assertEqual(6, part_two("1212"))
        self.assertEqual(0, part_two("1221"))
        self.assertEqual(4, part_two("123425"))
        self.assertEqual(12, part_two("123123"))
        self.assertEqual(4, part_two("12131415"))
        self.assertEqual(6, part_two(get_data("sample.txt")))
