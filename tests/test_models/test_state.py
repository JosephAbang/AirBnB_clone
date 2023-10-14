#!/usr/bin/python3
"""
TestFile for class State
"""

import unittest
from datetime import datetime as dt
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Class defines Test file for State
    Inherits from BaseModel
    """

    def test_name(self):
        new = State()
        new.name = "Kogi"
        self.assertEqual(type(new.name), str)

    def test_Updated_at_type(self):
        n = State()
        self.assertEqual(type(n.updated_at), type(dt.now()))

    def test_id_type(self):
        n = State()
        self.assertEqual(type(n.id), str)

    def test_dict_id(self):
        b = State()
        my_dict = b.to_dict()
        self.assertEqual(b.id, my_dict['id'])

    def test_dict_created_at(self):
        b = State()
        my_dict = b.to_dict()
        self.assertEqual(b.updated_at.isoformat(), my_dict['updated_at'])

    def test_class_name(self):
        b = State()
        my_dict = b.to_dict()
        self.assertEqual(type(b).__name__, my_dict['__class__'])

    def test_instance(self):
        b = State()
        self.assertIsInstance(State(), type(b))

    def test_save_updated_at(self):
        b = State()
        before = b.to_dict()
        b.save()
        after = b.to_dict()
        self.assertNotEqual(before['updated_at'], after['updated_at'])

    def test_save_created_at(self):
        b = State()
        before = b.to_dict()
        b.save()
        after = b.to_dict()
        self.assertEqual(before['created_at'], after['created_at'])

    def test_save_id(self):
        b = State()
        before = b.to_dict()
        b.save()
        after = b.to_dict()
        self.assertEqual(before['id'], after['id'])


if __name__ == "__main__":
    unittest.main()
