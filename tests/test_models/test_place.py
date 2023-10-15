#!/usr/bin/python3
"""
TestFile for class Place
"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Class defines Test file for Place
    Inherits from BaseModel
    """

    def test_city_id(self):
        """Test for city_id attribute in Place Class"""
        obj = Place()
        obj.city_id = "34233"
        self.assertEqual(type(obj.name), str)

    def test_user_id(self):
        """Test for user_id attribute in Place Class"""
        obj = Place()
        obj.user_id = "23423"
        self.assertEqual(type(obj.name), str)

    def test_name(self):
        """Test for name attribute in Place Class"""
        obj = Place()
        obj.name = "John Doe"
        self.assertEqual(type(obj.name), str)

    def test_description(self):
        """Test for description attribute in Place Class"""
        obj = Place()
        obj.description = "A two-bedroom apartment"
        self.assertEqual(type(obj.description), str)

    def test_number_rooms(self):
        """Test for number_rooms attribute in Place Class"""
        obj = Place()
        obj.number_rooms = 2
        self.assertEqual(type(obj.number_rooms), int)

    def test_number_bathrooms(self):
        """Test for number_bathrooms attribute in Place Class"""
        obj = Place()
        obj.number_bathrooms = 1
        self.assertEqual(type(obj.number_bathrooms), int)

    def test_max_guest(self):
        """Test for max_guest attribute in Place Class"""
        obj = Place()
        obj.max_guest = 1
        self.assertEqual(type(obj.max_guest), int)

    def test_price_by_night(self):
        """Test for price_by_night attribute in Place Class"""
        obj = Place()
        obj.price_by_night = 90
        self.assertEqual(type(obj.price_by_night), int)

    def test_latitude(self):
        """Test for latitude attribute in Place Class"""
        obj = Place()
        obj.latitude = 2.0
        self.assertEqual(type(obj.latitude), float)

    def test_longitude(self):
        """Test for longitude attribute in Place Class"""
        obj = Place()
        obj.longitude = 5.0
        self.assertEqual(type(obj.longitude), float)

    def test_amenity_ids(self):
        """Test for amenity_ids attribute in Place Class"""
        obj = Place()
        obj.amenity_ids = []
        self.assertEqual(type(obj.amenity_ids), list)


if __name__ == "__main__":
    unittest.main()
