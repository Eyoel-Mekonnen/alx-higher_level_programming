#!/usr/bin/python3
"""Testing the Rectangel class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """Unittest for testing Rectangle"""
    def test_is_instance_of_parent(self):
        rectangle = Rectangle(10, 2)
        self.assertIsInstance(rectangle, Base)
        self.assertEqual(10, rectangle.width)
        self.assertEqual(2, rectangle.height)
