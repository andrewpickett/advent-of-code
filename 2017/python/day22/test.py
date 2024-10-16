import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(5, part_one(get_data("sample.txt"), bursts=7))
		self.assertEqual(41, part_one(get_data("sample.txt"), bursts=70))
		self.assertEqual(5587, part_one(get_data("sample.txt"), bursts=10000))

	def test_part_two(self):
		self.assertEqual(26, part_two(get_data("sample.txt"), bursts=100))
		self.assertEqual(2511944, part_two(get_data("sample.txt"), bursts=10000000))
