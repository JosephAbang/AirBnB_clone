#!/usr/bin/python3

import unittest
from datetime import datetime as dt
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_Updated_at_type(self):
        b = BaseModel()
        self.assertEqual(type(b.updated_at), type(dt.now()))

    def test_created_at_type(self):
        b = BaseModel()
        self.assertEqual(type(b.created_at), type(dt.now()))

    def test_id_type(self):
        b = BaseModel()
        self.assertEqual(type(b.id), str)


if __name__ == "__main__":
    unittest.main()
