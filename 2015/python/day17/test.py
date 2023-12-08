import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		d = get_data("sample.txt")
		d["target"] = 25
		self.assertEqual(4, part_one(d))

	def test_part_two(self):
		d = get_data("sample.txt")
		d["target"] = 25
		self.assertEqual(3, part_two(d))
