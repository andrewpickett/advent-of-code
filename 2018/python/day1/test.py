import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(3, part_one(["+1", "+1", "+1"]))
		self.assertEqual(0, part_one(["+1", "+1", "-2"]))
		self.assertEqual(-6, part_one(["-1", "-2", "-3"]))
		self.assertEqual(3, part_one(get_data("sample.txt")))

	def test_part_two(self):
		self.assertEqual(0, part_two(["+1", "-1"]))
		self.assertEqual(10, part_two(["+3", "+3", "+4", "-2", "-4"]))
		self.assertEqual(5, part_two(["-6", "+3", "+8", "+5", "-6"]))
		self.assertEqual(14, part_two(["+7", "+7", "-2", "-7", "-4"]))
		self.assertEqual(2, part_two(get_data("sample.txt")))
