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
        rectangle2 = Rectangle(1, 2, 3)
        self.assertEqual(1, rectangle2.width)
        self.assertEqual(2, rectangle2.height)
        self.assertEqual(3, rectangle2.x)
        rectangle3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(1, rectangle3.width)
        self.assertEqual(2, rectangle3.height)
        self.assertEqual(3, rectangle3.x)
        self.assertEqual(4, rectangle3.y)
    
    def test_if_parameters_are_correct(self):
        """Checks wether or not passed parameters are integers."""
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle("1", 2)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(1, "2")
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, 3, "4")
        rectangle = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(1, rectangle.width)
        self.assertEqual(2, rectangle.height)
        self.assertEqual(3, rectangle.x)
        self.assertEqual(4, rectangle.y)
        self.assertEqual(5, rectangle.id)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(1, -2)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(1, 0)
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Rectangle(1, 2, 3, -4)

    def test_area_rectangle(self):
        """Test the area of rectangel."""
        rectangle = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(2, rectangle.area())
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(-1, 2, 3, 4, 5)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(1, -2, 3, 4, 5)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle("1", 2, 3, 4, 5)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(1, "2", 3, 4, 5) 


