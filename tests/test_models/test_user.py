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
        User.email = 'james.bond@gmail.com'
        User.first_name = 'James'
        User.last_name = 'Bond'
        User.password = '0000'


    def test_NameAttribut(self):
        # test value of attribut
        self.assertEqual(User.email, "james.bond@gmail.com")
        self.assertEqual(User.first_name, "James")
        self.assertEqual(User.last_name, "Bond")
        self.assertEqual(User.password, "0000")


    def test_SubclassBaseModel(self):
        # test is subclass
        self.assertTrue(issubclass(User, BaseModel))
