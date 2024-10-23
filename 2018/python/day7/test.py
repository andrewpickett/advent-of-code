import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		d = get_data("sample.txt")
		d["workers"] = 1
		d["timer"] = 0
		self.assertEqual("CABDFE", part_one(d))

	def test_part_two(self):
		d = get_data("sample.txt")
		d["workers"] = 2
		d["timer"] = 0
		self.assertEqual(15, part_two(d))
