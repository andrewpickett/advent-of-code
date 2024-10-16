import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(12, part_one(get_data("sample.txt"), iters=2))

	def test_part_two(self):
		# Part 2 is exactly the same as part one...and there is no new test data for me to use, and the given test data
		# doesn't work for more than 2 iterations...so...we'll just repeat it.
		self.assertEqual(12, part_two(get_data("sample.txt"), iters=2))
