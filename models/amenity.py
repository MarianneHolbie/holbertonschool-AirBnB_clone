#!/usr/bin/python3
"""
    Class Amenity inherit from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        Class User

        ATTRIBUTS
        ============

            name: public, amenity's name

            **kwargs: **kwargs of class BaseModel

    """

    name = ""
