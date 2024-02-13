import unittest

from main import part_one, part_two, get_data, get_ascii_vals


class TestMain(unittest.TestCase):

	def test_part_one(self):
		d = get_data("sample.txt")
		d["knot"] = [0, 1, 2, 3, 4]
		self.assertEqual(12, part_one(d))

	def test_part_two(self):
		d = {"knot": [x for x in range(256)], "ascii": get_ascii_vals("")}
		self.assertEqual("a2582a3a0e66e6e86e3812dcb672a272", part_two(d))
		d = {"knot": [x for x in range(256)], "ascii": get_ascii_vals("AoC 2017")}
		self.assertEqual("33efeb34ea91902bb2f59c9920caa6cd", part_two(d))
		d = {"knot": [x for x in range(256)], "ascii": get_ascii_vals("1,2,3")}
		self.assertEqual("3efbe78a8d82f29979031a4aa0b16a9d", part_two(d))
		d = {"knot": [x for x in range(256)], "ascii": get_ascii_vals("1,2,4")}
		self.assertEqual("63960835bcdc130f0b66d7ff4f6a5a8e", part_two(d))
