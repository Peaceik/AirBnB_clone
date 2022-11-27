#!/usr/bin/python3
"""This module tests the place model for edge cases
"""
import time
import json
import uuid
import os
import re
import unittest
from datetime import datetime as datetime
import sys
from models.place import Place
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
sys.path.append("..")


class TestPlace(unittest.TestCase):

    """Test Cases for the Place class."""

    p = Place()

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

    def test_instance(self):
        """Tests instantiation of Place class."""

        b = Place()
        self.assertEqual(str(type(b)), "<class 'models.place.Place'>")
        self.assertIsInstance(b, Place)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.p)), "<class 'models.place.Place'>")

    def test_user_inheritance(self):
        """test if Place is a subclass of BaseModel"""
        self.assertIsInstance(self.p, Place)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.p, 'city_id'))
        self.assertTrue(hasattr(self.p, 'user_id'))
        self.assertTrue(hasattr(self.p, 'name'))
        self.assertTrue(hasattr(self.p, 'description'))
        self.assertTrue(hasattr(self.p, 'number_rooms'))
        self.assertTrue(hasattr(self.p, 'number_bathrooms'))
        self.assertTrue(hasattr(self.p, 'max_guest'))
        self.assertTrue(hasattr(self.p, 'price_by_night'))
        self.assertTrue(hasattr(self.p, 'latitude'))
        self.assertTrue(hasattr(self.p, 'longitude'))
        self.assertTrue(hasattr(self.p, 'amenity_ids'))
        self.assertTrue(hasattr(self.p, 'id'))
        self.assertTrue(hasattr(self.p, 'created_at'))
        self.assertTrue(hasattr(self.p, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.p.city_id, str)
        self.assertIsInstance(self.p.user_id, str)
        self.assertIsInstance(self.p.name, str)
        self.assertIsInstance(self.p.description, str)
        self.assertIsInstance(self.p.number_rooms, int)
        self.assertIsInstance(self.p.number_bathrooms, int)
        self.assertIsInstance(self.p.max_guest, int)
        self.assertIsInstance(self.p.price_by_night, int)
        self.assertIsInstance(self.p.latitude, float)
        self.assertIsInstance(self.p.longitude, float)
        self.assertIsInstance(self.p.amenity_ids, list)
        self.assertIsInstance(self.p.id, str)
        self.assertIsInstance(self.p.created_at, datetime)
        self.assertIsInstance(self.p.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
