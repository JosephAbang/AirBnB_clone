#!/usr/bin/python3
"""
Module defines a class called User
User class inherits from BaseModel class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
