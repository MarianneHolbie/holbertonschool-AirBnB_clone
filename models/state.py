#!/usr/bin/python3
"""
    Class State inherit from BaseModel
"""
import models
from models.base_model import BaseModel
import models.engine.file_storage


class State(BaseModel):
    """
        Class User

        ATTRIBUTS
        ============

            name: public, state's name

            **kwargs: **kwargs of class BaseModel

    """

    name = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        models.storage.save()
        models.storage.new(self)
