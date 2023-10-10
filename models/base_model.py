#!/usr/bin/python3
"""
Module defines a class called BaseModel
BaseModel - base class of all our models
"""

import uuid
from datetime import datetime

class BaseModel:
    """base class of all our models"""

    id =  str(uuid.uuid4())
    created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
    updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """Method defines str representation of instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
