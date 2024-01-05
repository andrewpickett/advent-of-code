import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(0, part_one([(5, 12, 25)]))

	def test_part_two(self):
		self.assertEqual(6, part_two(get_data("sample.txt")))
