import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(41, part_one(get_data("sample.txt")))

	def test_part_two(self):
		d = get_data("sample.txt")
		part_one(d)
		self.assertEqual(6, part_two(d))
