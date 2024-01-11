import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		d = get_data("sample.txt")
		d["r"] = 10
		self.assertEqual(38, part_one(d))

	def test_part_two(self):
		self.assertEqual(1935478, part_two(get_data("sample.txt")))
