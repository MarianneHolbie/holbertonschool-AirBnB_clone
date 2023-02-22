#!/usr/bin/python3
"""
    Class Amenity inherit from BaseModel
"""
import models
from models.base_model import BaseModel
import models.engine.file_storage


class Amenity(BaseModel):
    """
        Class User

        ATTRIBUTS
        ============

            name: public, amenity's name

            **kwargs: **kwargs of class BaseModel

    """

    name = ""
