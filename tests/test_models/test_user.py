#!/usr/bin/python3
"""
Test file for class user
"""

import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime as dt


class TestUser(unittest.TestCase):
    """Tests the user class using unit testing
    Inherits from BaseModeol
    """

    def test_email(self):
        """Test email attribute type"""
        new = User()
        new.email = "Hellojoe@gmail.com"
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Test password attribute type"""
        new = User()
        new.password = "4dfff5tg5tGTtgds33#%"
        self.assertEqual(type(new.password), str)

    def test_first_name(self):
        """Test first_name attribute type"""
        new = User()
        new.first_name = "Jay"
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test last_name attribute type"""
        new = User()
        new.last_name = "Lewis"
        self.assertEqual(type(new.last_name), str)

    def test_init_id(self):
        """Test id attribute value uniqueness after save()"""
        new = User()
        before = new.to_dict()
        new.save()
        after = new.to_dict()
        self.assertEqual(before['id'], after['id'])


if __name__ == "__main__":
    unittest.main()
