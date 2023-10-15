#!/usr/bin/python3
"""
TestFile for class Review
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Class defines Test file for Review
    Inherits from BaseModel
    """

    def test_place_id(self):
        obj = Review()
        obj.place_id = "3324"
        self.assertEqual(type(obj.place_id), str)

    def test_user_id(self):
        obj = Review()
        obj.user_id = "24234"
        self.assertEqual(type(obj.user_id), str)

    def test_text(self):
        obj = Review()
        obj.text = "Nice confortable apartment"
        self.assertEqual(type(obj.text), str)


if __name__ == "__main__":
    unittest.main()
