import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		d = get_data("sample.txt")
		d["k"] = "abcde"
		self.assertEqual("decab", part_one(d))

	def test_part_two(self):
		pass
