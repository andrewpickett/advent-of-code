import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(4, part_one(["H => HO", "H => OH", "O => HH", "HOH"]))

	def test_part_two(self):
		self.assertEqual(6, part_two(get_data("sample.txt")))
