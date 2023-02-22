#!/usr/bin/python3
"""
    Class State inherit from BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
        Class User

        ATTRIBUTS
        ============

            name: public, state's name

            **kwargs: **kwargs of class BaseModel

    """

    name = ""
