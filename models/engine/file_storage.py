#!/usr/bin/python3
"""
Module contains a file named FileStorage
"""
import json
from datetime import datetime as dt


class FileStorage:
    """
    a class FileStorage that serializes instances to
    a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary `__objects`"""
        return FileStorage.__objects

    def new(self, obj):
        """sets dictionary key with id"""
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """serializes dictionary to the JSON file"""
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            ser_dict = {}
            ser_dict.update(FileStorage.__objects)
            for item in ser_dict:
                ser_dict[item] = ser_dict[item].to_dict()
            json.dump(ser_dict, f)

    def reload(self):
        """deserializes the JSON file to a dict"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        class_ = {'BaseModel': BaseModel,
                  'User': User,
                  'Place': Place,
                  'State': State,
                  'City': City,
                  'Amenity': Amenity,
                  'Review': Review}
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8")\
                    as f:
                data = json.load(f)
                for key, obj_dict in data.items():
                    FileStorage.__objects[key] = \
                            class_[obj_dict["__class__"]](**obj_dict)
        except FileNotFoundError:
            pass
