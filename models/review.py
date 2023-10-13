"""
Module defines class called Review
Review class inherits from BaseModel
"""

from base_model import BaseModel
from place import Place


class Review(BaseModel):
    """A Review class that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
