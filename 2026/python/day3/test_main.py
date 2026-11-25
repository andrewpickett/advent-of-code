import unittest

from day1.main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def setUp(self):
		self.sample_file = open("day1/sample.txt")

	def tearDown(self):
		self.sample_file.close()

	def test_part_one(self):
		self.assertEqual(None, part_one(get_data(self.sample_file)))

	def test_part_two(self):
		self.assertEqual(None, part_two(get_data(self.sample_file)))
