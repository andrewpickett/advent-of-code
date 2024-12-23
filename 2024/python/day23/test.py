import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(7, part_one(get_data("sample.txt")))

	def test_part_two(self):
		self.assertEqual("co,de,ka,ta", part_two(get_data("sample.txt")))
