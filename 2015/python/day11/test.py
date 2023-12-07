import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual("abcdffaa", part_one("abcdefgh"))
		self.assertEqual("ghjaabcc", part_one("ghijklmn"))
		self.assertEqual("abcdffaa", part_one(get_data("sample.txt")))

	def test_part_two(self):
		self.assertEqual("abcdffcc", part_two("abcdffaa"))
