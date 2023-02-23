#!/usr/bin.python3
"""
    Module of Unittests for models/review.py

"""

import unittest
from models.base_model import BaseModel
from models.review import Review
from models.engine.file_storage import FileStorage

class Test_User(unittest.TestCase):
    """
        Tests of the subclass Review, it inherit from BaseModel
    """

    def setUp(self):
        r1 = Review()
        self.place_id = "456"
        self.user_id = "456-456-456"
        self.text = "this is a review"

    def test_NameAttribut(self):
        # test value of attribut.
        self.assertEqual(self.place_id, "456")
        self.assertEqual(self.user_id, "456-456-456")
        self.assertEqual(self.text, "this is a review")

    def test_ReviewAttb(self):
        """ checks review's attributes """
        self.assertEqual(str, type(Review.place_id))
        self.assertEqual(str, type(Review.user_id))
        self.assertEqual(str, type(Review.text))

    def test_SubclassBaseModel(self):
        # test is subclass
        self.assertTrue(issubclass(Review, BaseModel))
