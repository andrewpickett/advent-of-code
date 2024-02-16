import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		d = get_data("sample.txt")
		d["programs"] = list("abcde")
		self.assertEqual("baedc", part_one(d))

	def test_part_two(self):
		d = get_data("sample.txt")
		d["programs"] = list("abcde")
		self.assertEqual("abcde", part_two(d))
