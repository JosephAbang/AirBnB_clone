#!/usr/bin/python3
"""
TestFile for class City
"""

import unittest
from datetime import datetime as dt
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Class defines Test file for City
    Inherits from BaseModel
    """

    def test_name(self):
        new = City()
        new.name = "Kaicee"
        self.assertEqual(type(new.name), str)

    def test_name(self):
        new = City()
        new.state_id = "809889hhgcs9898"
        self.assertEqual(type(new.name), str)

    def test_Updated_at_type(self):
        n = City()
        self.assertEqual(type(n.updated_at), type(dt.now()))

    def test_id_type(self):
        n = City()
        self.assertEqual(type(n.id), str)

    def test_dict_id(self):
        b = City()
        my_dict = b.to_dict()
        self.assertEqual(b.id, my_dict['id'])

    def test_dict_created_at(self):
        b = City()
        my_dict = b.to_dict()
        self.assertEqual(b.updated_at.isoformat(), my_dict['updated_at'])

    def test_class_name(self):
        b = City()
        my_dict = b.to_dict()
        self.assertEqual(type(b).__name__, my_dict['__class__'])

    def test_instance(self):
        b = City()
        self.assertIsInstance(City(), type(b))

    def test_save_updated_at(self):
        b = City()
        before = b.to_dict()
        b.save()
        after = b.to_dict()
        self.assertNotEqual(before['updated_at'], after['updated_at'])

    def test_save_created_at(self):
        b = City()
        before = b.to_dict()
        b.save()
        after = b.to_dict()
        self.assertEqual(before['created_at'], after['created_at'])

    def test_save_id(self):
        b = City()
        before = b.to_dict()
        b.save()
        after = b.to_dict()
        self.assertEqual(before['id'], after['id'])


if __name__ == "__main__":
    unittest.main()
