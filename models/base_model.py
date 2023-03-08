#!/usr/bin/env python3

"""A module that contains the base_model class"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ A base model class"""

    def __init__(self, *args, **kwargs):
        """initialise an instance of the base model"""

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        date_format = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, date_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)



    def __str__(self):
        """An infomal string representation of an object"""

        class_name = self.__class__.__name__

        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""

        class_name = self.__class__.__name__
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = class_name

        return dictionary
