#!/usr/bin.python3
"""
    Module of Unittests for models/state.py

"""

import unittest
from models.base_model import BaseModel
from models.state import State
import uuid
import os
from datetime import datetime
import models
from unittest.mock import patch
from models.engine.file_storage import FileStorage

class Test_State(unittest.TestCase):
    """
        Tests of the subclass State, it inherit from BaseModel
    """

    def setUp(self):
        state1 = State()
        self.name = 'Occitanie'

    def test_NameAttribut(self):
        # test value of attribut
        self.assertEqual(self.name, "Occitanie")

    def test_user(self):
        # test state name """
        self.assertEqual(str, type(State.name))

    def test_SubclassBaseModel(self):
        # test is subclass.
        self.assertTrue(issubclass(State, BaseModel))

