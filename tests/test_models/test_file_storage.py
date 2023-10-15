#!/usr/bin/python
"""
Test file for class FileStorage
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Class test for FileStorage using unit test"""
    def test_Objects_type(self):
        b = BaseModel()
        all_objs = storage.all()
        self.assertTrue(type(all_objs), dict)

    def test_key(self):
        """Tests the key of file_objects"""
        b = BaseModel()
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            key = obj_id
        self.assertEqual(key, f"{type(b).__name__}.{b.id}")

    def test_obj(self):
        """Tests the value of file_objects"""
        b = BaseModel()
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
        self.assertIsInstance(obj, BaseModel)


if __name__ == "__main__":
    unittest.main()
