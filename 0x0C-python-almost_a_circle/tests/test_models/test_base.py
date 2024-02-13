#!/usr/bin/python3
"""Defines unittest for base.py in models"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """Unittiest testing for base class."""
    def test_instantiation(self):
        base1 = Base()
        base2 = Base()
        id1 = base1.id
        id2 = base2.id
        self.assertEqual(id1, 1)
        self.assertEqual(id2, id1 + 1)
        base3 = Base(3)
        base4 = Base()
        id3 = base3.id
        id4 = base4.id
        self.assertEqual(id4, id3)
