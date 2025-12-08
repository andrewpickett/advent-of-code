import unittest

from day5.main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def setUp(self):
		self.sample_file = open("day5/sample.txt")

	def tearDown(self):
		self.sample_file.close()

	def test_part_one(self):
		self.assertEqual(3, part_one(get_data(self.sample_file)))

	def test_part_two(self):
		self.assertEqual(14, part_two(get_data(self.sample_file)))
