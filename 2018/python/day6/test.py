import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(17, part_one(get_data("sample.txt")))

	def test_part_two(self):
		d = get_data("sample.txt")
		d["d"] = 32
		self.assertEqual(16, part_two(d))
