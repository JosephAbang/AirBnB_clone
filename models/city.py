"""
Module defines class called City
City class inherits from BaseModel
"""

from base_model import BaseModel
from state import State


class City(BaseModel):
    """City class that inherits from BaseModel"""

    state_id = ""
    name = ""
