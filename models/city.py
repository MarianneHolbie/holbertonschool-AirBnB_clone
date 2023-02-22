#!/usr/bin/python3
"""
    Class City inherit from BaseModel
"""
import models
from models.base_model import BaseModel
import models.engine.file_storage


class City(BaseModel):
    """
        Class User

        ATTRIBUTS
        ============
            state_id: public, state's id -> State.id

            name: public, city's name

            **kwargs: **kwargs of class BaseModel

    """

    state_id = ""
    name = ""
