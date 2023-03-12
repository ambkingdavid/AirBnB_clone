#!/usr/bin/env python3
""" defines a file storage class"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ a class that defines file storage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        content = FileStorage.__objects
        file_content = {obj: content[obj].to_dict() for obj in content.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(file_content, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
           exists otherwise, do nothing, no exception should be raised)
        """
        try:

            with open(FileStorage.__file_path) as f:
                file_content = json.load(f)
                for obj in file_content.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
