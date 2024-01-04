import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(5, part_one([("R", 2), ("L", 3)]))
		self.assertEqual(2, part_one([("R", 2), ("R", 2), ("R", 2)]))
		self.assertEqual(12, part_one([("R", 5), ("L", 5), ("R", 5), ("R", 3)]))

	def test_part_two(self):
		self.assertEqual(4, part_two(get_data("sample.txt")))
