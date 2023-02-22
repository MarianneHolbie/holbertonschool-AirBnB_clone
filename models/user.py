#!/usr/bin/python3
"""
    Class User inherit from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
        Class User

        ATTRIBUTS
        ============

            email: public, user's email

            first_name: public, first name of user

            last_name: public, last name of user

            password: public, password of user

            **kwargs: **kwargs of class BaseModel

    """

    def __init__(self, email="", first_name="", last_name="", password="", **kwargs):

        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        super().__init__(**kwargs)
