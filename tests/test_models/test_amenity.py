#!/usr/bin.python3
"""
    Module of Unittests for models/amenity.py

"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import uuid
import os
from datetime import datetime
import models
from unittest.mock import patch

class Test_Amenity(unittest.TestCase):
    """
        Tests of the subclass Amenity, it inherit from BaseModel
    """

    def test_NameAttribut(self):
        am1 = Amenity(name="air conditioning")
        # test value of attribut
        self.assertEqual(am1.name, "air conditioning")

    def test_AmenityDict(self):
        created_at = datetime.now()
        created_at = created_at.isoformat()
        updated_at = datetime.now()
        updated_at = updated_at.isoformat()
        am1 = Amenity(name="air conditioning", id=uuid.uuid4(), created_at=created_at, updated_at= updated_at)
        d = am1.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d['__class__'], 'Amenity')
        self.assertEqual(d['name'], 'air conditioning')