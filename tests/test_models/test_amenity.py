#!/usr/bin/python3
"""This module tests the amenity model for edge cases
"""
import time
import json
import uuid
import os
import re
import unittest
from datetime import datetime as datetime
import sys
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
sys.path.append("..")


class TestAmenity(unittest.TestCase):
    """The module tests the module in edge cases"""

    a = Amenity()

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_Amenity(self):
        """Tests instantiation of Amenity class."""

        a = Amenity()
        self.assertEqual(str(type(a)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(a, Amenity)
        self.assertTrue(issubclass(type(a), BaseModel))

    def test_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.a)), res)

    def test_user_inheritance(self):
        """test if Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.a, Amenity)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.a, 'name'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime)
        self.assertIsInstance(self.a.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
