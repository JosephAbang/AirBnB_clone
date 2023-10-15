#!/usr/bin/python3
"""
TestFile for Amenity class
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Class defines Test file for Amenity
    Inherits from BaseModel
    """

    def test_name(self):
        """Test for name attribute in Amenity Class"""
        obj = Amenity()
        obj.name = "Wayne Dave"
        self.assertEqual(type(obj.name), str)


if __name__ == "__main__":
    unittest.main()
