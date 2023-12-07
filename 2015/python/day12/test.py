import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		self.assertEqual(6, part_one('[1,2,3]'))
		self.assertEqual(6, part_one('{"a":2,"b":4}'))
		self.assertEqual(3, part_one('[[[3]]]'))
		self.assertEqual(3, part_one('{"a":{"b":4},"c":-1}'))
		self.assertEqual(0, part_one('[]'))
		self.assertEqual(0, part_one('{}'))
		self.assertEqual(3, part_one(get_data("sample.txt")))

	def test_part_two(self):
		self.assertEqual(6, part_two('[1,2,3]'))
		self.assertEqual(4, part_two('[1,{"c":"red","b":2},3]'))
		self.assertEqual(0, part_two('{"d":"red","e":[1,2,3,4],"f":5}'))
		self.assertEqual(6, part_two('[1,"red",5]'))
