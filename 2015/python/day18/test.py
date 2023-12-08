import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		d = get_data("sample.txt")
		d["steps"] = 4
		self.assertEqual(4, part_one(d))

	def test_part_two(self):
		d = get_data("sample.txt")
		d["steps"] = 5
		self.assertEqual(17, part_two(d))
