#!/usr/bin/python3
"""This module tests the base model for edge cases
"""


import sys
import unittest
from datetime import datetime as datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json
import uuid
import os
import re
sys.path.append("..")


class TestBaseModel(unittest.TestCase):
    """test cases for the base model class
    """

    my_model = BaseModel()

    def setup(self):
        """prepare the test methods"""
        pass

    def deleteSetup(self):
        """deletes test methods"""
        self.resetstorage()
        pass

    def resetStorage(self):
        """resets file storage data for the test methods"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_base_init(self):
        """
        Testing a class BaseModel
        """
        one = BaseModel()
        self.assertIsInstance(one, BaseModel)
        self.assertTrue(issubclass(type(one), BaseModel))
        self.assertIs(type(one), BaseModel)
        one.name = "Monday"
        one.my_number = 89
        self.assertEqual(one.name, "Monday")
        self.assertEqual(one.my_number, 89)

    def test_base_init_without_parameters(self):
        """Tests __init__ with no parameters"""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "__init__() missing 1 required "
        msg += "positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_str(self):
        """Test the string printing format method"""
        two = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(str(two))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), two.id)

    def test_save(self):
        """Tests the saving method without any parameters passed"""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_save_parameters(self):
        """Tests the saving method with more parameters/args passed"""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, "Parameter")
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_to_dict(self):
        """Tests the conversion method for dictionaries"""
        a = BaseModel()
        a.name = "ALX"
        a.age = 4
        b = a.to_dict()
        self.assertEqual(b["id"], a.id)
        self.assertEqual(b["created_at"], a.created_at.isoformat())
        self.assertEqual(b["updated_at"], a.updated_at.isoformat())
        self.assertEqual(b["name"], a.name)
        self.assertEqual(b["age"], a.age)

    def test_to_dict_without_parameters(self):
        """Tests to_dict() with no parameters passed."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        msg = "to_dict() missing 1 required "
        msg += "positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_3_to_dict_more_parameters(self):
        """Tests to_dict() with more parameters."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, "work", "serve", "love")
        msg = "to_dict() takes 1 positional "
        msg += "argument but 4 were given"
        self.assertEqual(str(e.exception), msg)

    def test_instantiation_process(self):
        """Tests instantiation with **kwargs."""
        b = BaseModel()
        b.name = "ALX"
        b.my_number = 4
        b_json = b.to_dict()
        b_new = BaseModel(**b_json)
        self.assertEqual(b_new.to_dict(), b.to_dict())

    def testBaseModel1(self):
        """ Test attributes value of a BaseModel instance """

        self.my_model.name = "Holberton"
        self.my_model.my_number = 89
        self.my_model.save()
        my_model_json = self.my_model.to_dict()

        self.assertEqual(self.my_model.name, my_model_json['name'])
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.my_model.id, my_model_json['id'])

    def testSave(self):
        """ Checks if save method updates the public instance instance
        attribute updated_at """
        self.my_model.first_name = "First"
        self.my_model.save()

        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

        first_dict = self.my_model.to_dict()

        self.my_model.first_name = "Second"
        self.my_model.save()
        sec_dict = self.my_model.to_dict()

        self.assertEqual(first_dict['created_at'], sec_dict['created_at'])
        self.assertNotEqual(first_dict['updated_at'], sec_dict['updated_at'])


if __name__ == '__main__':
    unittest.main()
