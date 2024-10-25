import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

	def test_part_one(self):
		s = "\n#   #  ###\n#   #   # \n#   #   # \n#####   # \n#   #   # \n#   #   # \n#   #   # \n#   #  ###\n"
		self.assertEqual(s, part_one(get_data("sample.txt")))

	def test_part_two(self):
		self.assertEqual(3, part_two(get_data("sample.txt")))
