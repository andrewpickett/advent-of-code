import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		d = get_data("sample.txt")
		d["savings"] = 40
		self.assertEqual(2, part_one(d))

	def test_part_two(self):
		d = get_data("sample.txt")
		d["savings"] = 50
		self.assertEqual(285, part_two(d))
