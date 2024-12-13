import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		d = get_data("sample.txt")
		d["input"] = d["instructions"][1:3]
		self.assertEqual(30, part_one(d))

	def test_part_two(self):
		d = get_data("sample.txt")
		d["input"] = d["instructions"][1:3]
		d["target"] = 30
		self.assertEqual(0, part_two(d))
