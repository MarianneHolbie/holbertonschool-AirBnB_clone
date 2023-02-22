#!/usr/bin/python3
"""
    Class Review inherit from BaseModel
"""
import models
from models.base_model import BaseModel
import models.engine.file_storage
from models.amenity import Amenity
from models.place import Place
from models.user import User


class Review(BaseModel):
    """
        Class Review

        ATTRIBUTS
        ============
            place_id: public, place's id -> Place.id

            user_id: public, user's id -> User.id

            text: public, text of review

            **kwargs: **kwargs of class BaseModel

    """

    place_id = ""
    user_id = ""
    text = ""
