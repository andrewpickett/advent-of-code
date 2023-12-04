import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(1000000, part_one(["turn on 0,0 through 999,999"]))
		self.assertEqual(1000, part_one(["toggle 0,0 through 999,0"]))
		self.assertEqual(0, part_one(["turn off 499,499 through 500,500"]))

	def test_part_two(self):
		self.assertEqual(1, part_two(["turn on 0,0 through 0,0"]))
		self.assertEqual(2000000, part_two(get_data("sample.txt")))
