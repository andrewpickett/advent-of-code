import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual("5158916779", part_one(get_data("sample.txt")))
		self.assertEqual("0124515891", part_one(5))
		self.assertEqual("9251071085", part_one(18))
		self.assertEqual("5941429882", part_one(2018))

	def test_part_two(self):
		self.assertEqual("9", part_two("51589"))
		self.assertEqual("5", part_two("01245"))
		self.assertEqual("18", part_two("92510"))
		self.assertEqual("2018", part_two("59414"))
