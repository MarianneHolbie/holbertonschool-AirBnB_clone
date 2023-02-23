#!/usr/bin.python3
"""
    Module of Unittests for models/place.py

"""

import unittest
from models.base_model import BaseModel
from models.place import Place
from models.engine.file_storage import FileStorage
import models
import datetime

class Test_User(unittest.TestCase):
    """
        Tests of the subclass Place, it inherit from BaseModel
    """

    def setUp(self):
        p1 = Place()
        self.city_id = "456"
        self.user_id = "456-456-456"
        self.name = "Villa Bleue"
        self.description = "Magnifique maison en bord de mer"
        self.number_rooms = 5
        self.number_bathrooms = 5
        self.max_guest = 10
        self.price_by_night = 250
        self.latitude = 56.85
        self.longitude = 87.65
        self.amenity_ids = ["piscine", "air conditionné", "salle de bain individuelles"]


    def test_NameAttribut(self):
        # test value of attribut.
        self.assertEqual(self.city_id, "456")
        self.assertEqual(self.user_id, "456-456-456")
        self.assertEqual(self.name, "Villa Bleue")
        self.assertEqual(self.description, "Magnifique maison en bord de mer")
        self.assertEqual(self.number_rooms, 5)
        self.assertEqual(self.number_bathrooms, 5)
        self.assertEqual(self.max_guest, 10)
        self.assertEqual(self.price_by_night, 250)
        self.assertEqual(self.latitude, 56.85)
        self.assertEqual(self.longitude, 87.65)
        self.assertIn("piscine", self.amenity_ids)
        self.assertIn("air conditionné", self.amenity_ids)
        self.assertIn("salle de bain individuelles", self.amenity_ids)
        self.assertTrue(type(self.amenity_ids), list)

    def test_SubclassBaseModel(self):
        # test is subclass
        self.assertTrue(issubclass(Place, BaseModel))

    def test_no_args_instantiates(self):
        # test right type
        self.assertEqual(Place, type(Place()))

    def test_NewInstanceStored_inObjects(self):
        # new instance save in __objects
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        # test type of id
        self.assertEqual(str, type(Place().id))

    def test_CityId_PublicClassAttb(self):
        # test city_id public
        pl = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pl))
        self.assertNotIn("city_id", pl.__dict__)

    def test_UserId_PublicClassAttb(self):
        # test user_id public
        pl = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pl))
        self.assertNotIn("user_id", pl.__dict__)

    def test_Name_PublicAttb(self):
        # test name is public attribut
        pl = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(pl))
        self.assertNotIn("name", pl.__dict__)

    def test_Description_PublicAttb(self):
        # test description is public attribut
        pl = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(pl))
        self.assertNotIn("desctiption", pl.__dict__)

    def test_NumberRoom_PublicAttb(self):
        # test number_rooms is public attribut
        pl = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(pl))
        self.assertNotIn("number_rooms", pl.__dict__)

    def test_NumberBathroom_PublicAttb(self):
        # test number_bathrooms is public attribut
        pl = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl))
        self.assertNotIn("number_bathrooms", pl.__dict__)

    def test_MaxGuest__PublicAttb(self):
        # test max_guest is public attribut
        pl = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(pl))
        self.assertNotIn("max_guest", pl.__dict__)

    def test_PriceNight_PublicAttb(self):
        # test price_by_night is public attribut
        pl = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(pl))
        self.assertNotIn("price_by_night", pl.__dict__)

    def test_Latitude_PublicAttb(self):
        # test latitude is public attribut
        pl = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(pl))
        self.assertNotIn("latitude", pl.__dict__)

    def test_Longitude_PublicAttb(self):
        # test longitude is public attribut
        pl = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(pl))
        self.assertNotIn("longitude", pl.__dict__)

    def test_AmenityIds_PublicAttb(self):
        # test amenity_ids is public attribut
        pl = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(pl))
        self.assertNotIn("amenity_ids", pl.__dict__)