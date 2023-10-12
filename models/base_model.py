#!/usr/bin/python3
"""
Module defines a class called BaseModel
BaseModel - base class of all our models
"""

import uuid
from datetime import datetime as dt
from models import storage


class BaseModel:
    """base class of all our models"""

    def __init__(self, *args, **kwargs):
        """Initializes public class attributes"""
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == "created_at":
                        value = dt.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    if key == "updated_at":
                        value = dt.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            self.name = "Josh"
            storage.new(self)

    def __str__(self):
        """Method defines str representation of instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Method updates the public instance attribute `updated_at`"""
        self.updated_at = dt.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict
