import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		d = {"registers": {"a": 0, "b": 0, "c": 9}, "inst": [2,6]}
		part_one(d)
		self.assertEqual(1, d["registers"]["b"])

		d = {"registers": {"a": 10, "b": 0, "c": 0}, "inst": [5,0,5,1,5,4]}
		self.assertEqual("0,1,2", part_one(d))

		d = {"registers": {"a": 2024, "b": 0, "c": 0}, "inst": [0,1,5,4,3,0]}
		self.assertEqual("4,2,5,6,7,7,7,7,3,1,0", part_one(d))
		self.assertEqual(0, d["registers"]["a"])

		d = {"registers": {"a": 0, "b": 29, "c": 0}, "inst": [1,7]}
		part_one(d)
		self.assertEqual(26, d["registers"]["b"])

		d = {"registers": {"a": 0, "b": 2024, "c": 43690}, "inst": [4,0]}
		part_one(d)
		self.assertEqual(44354, d["registers"]["b"])

		self.assertEqual("4,6,3,5,6,3,5,2,1,0", part_one(get_data("sample.txt")))


	def test_part_two(self):
		# Since this was a deconstruction specific to my input, I don't have any unit tests for this one.
		pass
