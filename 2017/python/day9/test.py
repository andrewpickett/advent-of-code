import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(1, part_one("{}"))
		self.assertEqual(6, part_one("{{{}}}"))
		self.assertEqual(5, part_one("{{},{}}"))
		self.assertEqual(16, part_one("{{{},{},{{}}}}"))
		self.assertEqual(1, part_one("{<a>,<a>,<a>,<a>}"))
		self.assertEqual(9, part_one("{{<ab>},{<ab>},{<ab>},{<ab>}}"))
		self.assertEqual(9, part_one("{{<!!>},{<!!>},{<!!>},{<!!>}}"))
		self.assertEqual(3, part_one("{{<a!>},{<a!>},{<a!>},{<ab>}}"))
		self.assertEqual(0, part_one(get_data("sample.txt")))

	def test_part_two(self):
		self.assertEqual(10, part_two("<{o'i!a,<{i<a>"))
		self.assertEqual(10, part_two(get_data("sample.txt")))
