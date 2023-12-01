import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(58, part_one([(2, 3, 4)]))
		self.assertEqual(43, part_one([(1, 1, 10)]))
		self.assertEqual(101, part_one(get_data("sample.txt")))

	def test_part_two(self):
		self.assertEqual(34, part_two([(2, 3, 4)]))
		self.assertEqual(14, part_two([(1, 1, 10)]))
		self.assertEqual(48, part_two(get_data("sample.txt")))
