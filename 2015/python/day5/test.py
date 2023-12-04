import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(1, part_one(["ugknbfddgicrmopn"]))
		self.assertEqual(1, part_one(["aaa"]))
		self.assertEqual(0, part_one(["jchzalrnumimnmhp"]))
		self.assertEqual(0, part_one(["haegwjzuvuyypxyu"]))
		self.assertEqual(0, part_one(["dvszwmarrgswjxmb"]))

	def test_part_two(self):
		self.assertEqual(1, part_two(["qjhvhtzxzqqjkmpb"]))
		self.assertEqual(1, part_two(["xxyxx"]))
		self.assertEqual(0, part_two(["uurcxstgmygtbstg"]))
		self.assertEqual(0, part_two(["ieodomkazucvgmuy"]))
		self.assertEqual(2, part_two(get_data("sample.txt")))
