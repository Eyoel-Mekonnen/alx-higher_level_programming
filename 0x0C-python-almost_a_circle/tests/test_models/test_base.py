#!/usr/bin/python3
"""Defines unittest for base.py in models"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """Unittiest testing for base class."""
    def test_instantiation(self):
        """Test the instantiattion of Base ID"""
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
    
    def test_base_id(self):
        """Checks if specified id is assigned correctly."""
        base1 = Base(89)
        self.assertEqual(base1.id, 89)

    def test_to_json_string(self):
        """checks if the json_to_string handles none or empty string"""
        base = Base()
        self.assertEqual(base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        """Checks if to_json_string handles empty list and type."""
        base = Base()
        self.assertEqual("[]", base.to_json_string([]))
        self.assertEqual(base.to_json_string([ { 'id': 12 }]), '[{"id": 12}]')
        self.assertEqual(str, type(base.to_json_string([ { 'id': 12 }])))

    def test_from_json_string_none(self):
        """checks if empty is handled."""
        base = Base(4)
        self.assertEqual([], base.from_json_string(None))
        self.assertEqual([], base.from_json_string(None))

    def test_from_json_string_with_value(self):
        """Checks how the valued are displayed."""
        base = Base(6)
        self.assertEqual([{"id": 89}], base.from_json_string('[{ "id": 89 }]'))
        self.assertEqual(list, type(base.from_json_string('[{ "id": 89 }]')))
