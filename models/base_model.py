#!/usr/bin/python3
""" This module contains a base model for all other models """
import uuid
from datetime import datetime


class BaseModel(object):
    """
    Base model for all other models to inherit from

    Attributes:
    id(str) - unique string id
    created_at(datetime) - time object was created
    updated_at(datetime) - last time object was updated

    Methods:
    save - save an object and updates the time
    to_dict - returns a dictionary representation of object
    """
    def __init__(self) -> None:
        """ initialize BaseModel instance """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """ save the instance and update the time """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ create and return a dictionary representation of the object """
        my_dict = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                my_dict[key] = value.isoformat()
            my_dict[key] = value
        my_dict["__class__"] = self.__class__.__name__

        return my_dict

    def __str__(self) -> str:
        """ string representation of object """
        string = "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)
        return string
