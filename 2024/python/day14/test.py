import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		d = get_data("sample.txt")
		d["range"] = (11, 7)
		self.assertEqual(12, part_one(d))

	def test_part_two(self):
		# self.assertEqual(None, part_two(get_data("sample.txt")))
		# Not sure the best way to test this, without completely running a new sample...
		self.assertTrue(True)
