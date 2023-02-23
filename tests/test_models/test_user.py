#!/usr/bin.python3
"""
    Module of Unittests for models/user.py

"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

class Test_User(unittest.TestCase):
    """
        Tests of the subclass User, it inherit from BaseModel
    """

    def setUp(self):
        u1 = User()
        self.email = 'james.bond@gmail.com'
        self.first_name = 'James'
        self.last_name = 'Bond'
        self.password = '0000'


    def test_NameAttribut(self):
        # test value of attribut
        self.assertEqual(self.email, "james.bond@gmail.com")
        self.assertEqual(self.first_name, "James")
        self.assertEqual(self.last_name, "Bond")
        self.assertEqual(self.password, "0000")


    def test_SubclassBaseModel(self):
        # test is subclass
        self.assertTrue(issubclass(User, BaseModel))
