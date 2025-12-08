import unittest

from day8.main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def setUp(self):
		self.sample_file = open("day8/sample.txt")

	def tearDown(self):
		self.sample_file.close()

	def test_part_one(self):
		d = get_data(self.sample_file)
		d["links"] = 10
		self.assertEqual(40, part_one(d))

	def test_part_two(self):
		self.assertEqual(25272, part_two(get_data(self.sample_file)))
