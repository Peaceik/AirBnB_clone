#!/usr/bin/python3
"""
class FileStorage that serializes instances to a JSON file and deserializes
JSON file to instances
"""
import json
import os


class FileStorage:
    """ serializes and deserializes json file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return dict __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)
        """
        dictionary = {}

        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dictionary, f)

    def delete(self, id):
        """ deletes an instance from the file storage """
        if id in FileStorage.__objects:
            FileStorage.__objects.pop(id)
            self.save()
            return True
        else:
            return False

    def reload(self):
        """ deserializes the JSON file to __objects
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        attr = {'BaseModel': BaseModel,
                "User": User,
                "Place": Place,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for value in json.load(f).values():
                    self.new(attr[value['__class__']](**value))
