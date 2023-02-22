#!/usr/bin/python3
"""
    Class User inherit from BaseModel
"""
import models
from models.base_model import BaseModel
import models.engine.file_storage


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
        super().__init__(**kwargs)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        models.storage.save()
