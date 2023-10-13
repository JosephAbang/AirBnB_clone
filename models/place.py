"""
Module defines class called Place
Place class inherits from BaseModel
"""

from base_model import BaseModel
from city import City
from user import User
from amenity import Amenity


class Place(BaseModel):
    """A Place class that inherits from BaseModel"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""
