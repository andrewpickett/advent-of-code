import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(2, part_one([12]))
		self.assertEqual(2, part_one([14]))
		self.assertEqual(654, part_one([1969]))
		self.assertEqual(33583, part_one(get_data("sample.txt")))

	def test_part_two(self):
		self.assertEqual(2, part_two([14]))
		self.assertEqual(966, part_two([1969]))
		self.assertEqual(50346, part_two([100756]))
