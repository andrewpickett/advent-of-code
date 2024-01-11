import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual("DDRRRD", part_one("ihgpwlah"))
		self.assertEqual("DDUDRLRRUDRD", part_one("kglvqrro"))
		self.assertEqual("DRURDRUDDLLDLUURRDULRLDUUDDDRR", part_one(get_data("sample.txt")))

	def test_part_two(self):
		self.assertEqual(370, part_two("ihgpwlah"))
		self.assertEqual(492, part_two("kglvqrro"))
		self.assertEqual(830, part_two(get_data("sample.txt")))
