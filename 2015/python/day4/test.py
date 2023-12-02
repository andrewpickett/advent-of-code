import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(609043, part_one("abcdef"))
		self.assertEqual(1048970, part_one("pqrstuv"))
		self.assertEqual(1048970, part_one(get_data("sample.txt")))

	def test_part_two(self):
		pass
		# self.assertEqual(3, part_two("^v"))
