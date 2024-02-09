import unittest

from main import part_one, part_two, get_data


class TestMain(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(2, part_one([["aa", "bb", "cc", "dd", "ee"], ["aa", "bb", "cc", "dd", "aa"], ["aa", "bb", "cc", "dd", "aaa"]]))
        self.assertEqual(2, part_one(get_data("sample1.txt")))

    def test_part_two(self):
        self.assertEqual(3, part_two([["abcde", "fghij"], ["abcde", "xyz", "ecdab"], ["a", "ab", "abc", "abd", "abf", "abj"], ["iiii", "oiii", "ooii", "oooi", "oooo"], ["oiii", "ioii", "iioi", "iiio"]]))
        self.assertEqual(3, part_two(get_data("sample2.txt")))
