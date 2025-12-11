import unittest

from day11.main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.sample_file = open("day11/sample.txt")
		self.assertEqual(5, part_one(get_data(self.sample_file)))
		self.sample_file.close()

	def test_part_two(self):
		self.sample_file = open("day11/sample2.txt")
		self.assertEqual(2, part_two(get_data(self.sample_file)))
		self.sample_file.close()
