#!/usr/bin/python3
"""This module tests the state model for edge cases
"""
import time
import json
import uuid
import os
import re
import unittest
from datetime import datetime as datetime
import sys
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
sys.path.append("..")


class TestState(unittest.TestCase):
    """Test Cases for the State class."""

    s = State()

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
        """Tests instantiation of State class."""

        b = State()
        self.assertEqual(str(type(b)), "<class 'models.state.State'>")
        self.assertIsInstance(b, State)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.s)), res)

    def test_user_inheritance(self):
        """test if State is a subclass of BaseModel"""
        self.assertIsInstance(self.s, State)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.s, 'name'))
        self.assertTrue(hasattr(self.s, 'id'))
        self.assertTrue(hasattr(self.s, 'created_at'))
        self.assertTrue(hasattr(self.s, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.s.name, str)
        self.assertIsInstance(self.s.id, str)
        self.assertIsInstance(self.s.created_at, datetime)
        self.assertIsInstance(self.s.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
