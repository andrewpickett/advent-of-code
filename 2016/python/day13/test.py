import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		d = get_data("sample.txt")
		d["t"] = (4, 7)
		self.assertEqual(11, part_one(d))

	def test_part_two(self):
		self.assertEqual(151, part_two(get_data("sample.txt")))
