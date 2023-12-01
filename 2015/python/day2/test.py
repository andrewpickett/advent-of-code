import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(0, part_one("(())"))
		self.assertEqual(0, part_one("()()"))
		self.assertEqual(3, part_one("((("))
		self.assertEqual(3, part_one("(()(()("))
		self.assertEqual(3, part_one("))((((("))
		self.assertEqual(-1, part_one("())"))
		self.assertEqual(-1, part_one("))("))
		self.assertEqual(-3, part_one(")))"))
		self.assertEqual(-3, part_one(")())())"))
		self.assertEqual(-3, part_one(get_data("sample.txt")))

	def test_part_two(self):
		self.assertEqual(1, part_two(")"))
		self.assertEqual(5, part_two("()())"))
