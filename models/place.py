#!/usr/bin/python3
"""
    Class Place inherit from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
        Class Place

        ATTRIBUTS
        ==============

            city_id: public id of the City

            user_id: public, User.id

            name: name of the City

            description: public, description of the City

            number_rooms: public, number of rooms in this place

            number_bathrooms: public, number bathroom in this place

            max_guest: public, number max of guest in this place

            price_by_night: public, price by night of rent

            latitude: public, float latitude

            longitude: public, float longitude

            amenity_ids: list of Amenity.id

            **kwargs: **kwargs of class BaseModel

    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
