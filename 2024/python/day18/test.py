import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		d = get_data("sample.txt")
		d["s"] = 7
		d["b"] = 12
		self.assertEqual(22, part_one(d))

	def test_part_two(self):
		d = get_data("sample.txt")
		d["s"] = 7
		d["b"] = 12
		self.assertEqual("6,1", part_two(d))
