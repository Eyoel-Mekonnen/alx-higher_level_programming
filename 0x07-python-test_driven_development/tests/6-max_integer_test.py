#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defining unittest for different scenarios"""

    def test_ordered_list(self):
        """To check for ordered lists"""
        list_t = [1, 2, 3, 4]
        self.assertEqual(max_integer(list_t), 4)

    def test_unordered_list(self):
        """To check for unordered lists"""
        list_t1 = [4, 3, 2, 1]
        self.assertEqual(max_integer(list_t1), 4)

    def test_empty_list(self):
        """To check return of empty list"""
        list_t2 = []
        self.assertEqual(max_integer(list_t2), None)

    def test_single_element(self):
        """To check if only one element is passed"""
        list_t3 = [5]
        self.assertEqual(max_integer(list_t3), 5)

    def test_float_list(self):
        """To check on float numbers"""
        list_t4 = [1.05, 2.75, 3.9, 0.75]
        self.assertEqual(max_integer(list_t4), 3.9)

    def test_negative_list(self):
        """To check it on negative numbers list and floats"""
        list_t5 = [-5, -2, -9, -10.3]
        self.assertEqual(max_integer(list_t5), -2)

    def test_string_list(self):
        """To check on strings list"""
        list_t6 = ["Eyoel", "is", "my", "name"]
        self.assertEqual(max_integer(list_t6), "name")

    def test_string(self):
        """To check on string"""
        list_t7 = "Eyoel"
        self.assertEqual(max_integer(list_t7), 'y')

    def test_empty(self):
        """To check on emtpy list"""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
