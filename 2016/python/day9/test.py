import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(6, part_one("ADVENT"))
		self.assertEqual(7, part_one("A(1x5)BC"))
		self.assertEqual(9, part_one("(3x3)XYZ"))
		self.assertEqual(11, part_one("A(2x2)BCD(2x2)EFG"))
		self.assertEqual(6, part_one("(6x1)(1x3)A"))
		self.assertEqual(18, part_one("X(8x2)(3x3)ABCY"))

	def test_part_two(self):
		self.assertEqual(445, part_two(get_data("sample.txt")))
		self.assertEqual(9, part_two("(3x3)XYZ"))
		self.assertEqual(20, part_two("X(8x2)(3x3)ABCY"))
		self.assertEqual(241920, part_two("(27x12)(20x12)(13x14)(7x10)(1x12)A"))
		self.assertEqual(445, part_two("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"))
