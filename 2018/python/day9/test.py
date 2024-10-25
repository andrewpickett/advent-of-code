import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(8317, part_one(get_data("sample.txt")))
		self.assertEqual(146373, part_one({"p": 13, "s": 7999}))
		self.assertEqual(2764, part_one({"p": 17, "s": 1104}))
		self.assertEqual(54718, part_one({"p": 21, "s": 6111}))
		self.assertEqual(37305, part_one({"p": 30, "s": 5807}))

	def test_part_two(self):
		self.assertEqual(74765078, part_two(get_data("sample.txt")))
