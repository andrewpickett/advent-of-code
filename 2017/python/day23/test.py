import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		# No sample data/tests available.
		self.assertEqual(1, part_one(get_data("sample.txt")))

	def test_part_two(self):
		# No sample data/tests available.
		self.assertEqual(0, part_two(get_data("sample.txt")))
