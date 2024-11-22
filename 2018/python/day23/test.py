import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(7, part_one(get_data("sample.txt")))

	def test_part_two(self):
		self.assertEqual(36, part_two([(10,12,12,2), (12,14,12,2), (16,12,12,4), (14,14,14,6), (50,50,50,200), (10,10,10,5)]))
