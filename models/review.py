#!/usr/bin/python3
"""
Module defines class called Review
Review class inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A Review class that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
