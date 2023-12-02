import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(8, part_one([
			"3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
			"1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
			"8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
			"1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
			"6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]))
		self.assertEqual(8, part_one(get_data("sample.txt")))

	def test_part_two(self):
		self.assertEqual(2286, part_two([
			"3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
			"1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
			"8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
			"1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
			"6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]))
		self.assertEqual(2286, part_two(get_data("sample.txt")))
