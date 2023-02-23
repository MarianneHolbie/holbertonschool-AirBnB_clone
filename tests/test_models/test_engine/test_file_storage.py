#!/usr/bin/python3
"""
    testing methods in file_storage
"""


import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Testfilepath(unittest.TestCase):


    def test_file_path_exists(self):
        # test if the path exists
        _file_path = ''

    def test_file_path_is_str(self):
        # test if the path of the file is a string
        __file_path = ''

    def test_file_path_json(self):
        # test if the path of the file is in json
        FileStorage._file_path = 'file.json'
        self.assertTrue(FileStorage._file_path == 'file.json')

    def test_file_path_no_json(self):
        # test if the path of the file is in json
        _file_path = 'file.json'
        self.assertFalse(FileStorage._file_path == 'file')


class Testobjects(unittest.TestCase):

    def test_objects_is_dict(self):
        # test if objects are in a dictionary in ouput
        __objects = {'my_number': 89}
        self.assertTrue(type(__objects) is dict)

    def test_add_objects(self):
        # test if add an objects in dict __objects with a key nameclass.id
        file_storage = FileStorage()
        base_model = BaseModel()
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertEqual(file_storage._FileStorage__objects[key], base_model)


class Testall(unittest.TestCase):

    def test_all_with_objects(self):
        # test if the dictionary is stored in __objects.
        file_storage = FileStorage()
        base_model = BaseModel()
        objects = file_storage.all()
        self.assertIn("{}.{}".format(
            base_model.__class__.__name__, base_model.id), objects)
        self.assertEqual(objects["{}.{}".format(
            base_model.__class__.__name__, base_model.id)], base_model)


class Testnew(unittest.TestCase):

    def test_new_with_objects(self):
        file_storage = FileStorage()
        base_model = BaseModel()
        objects = file_storage.all()
        self.assertIn("{}.{}".format(
            base_model.__class__.__name__, base_model.id), objects)
        self.assertEqual(objects["{}.{}".format(
            base_model.__class__.__name__, base_model.id)], base_model)


class Testsave(unittest.TestCase):

    def test_save_json_format(self):
        # test if save method saves objects in JSON format
        file_storage = FileStorage()
        base_model = BaseModel()
        file_storage.save()
        with open("file.json", "r") as f:
            data = json.load(f)
            self.assertIn("{}.{}".format(
                base_model.__class__.__name__, base_model.id), data)
            self.assertEqual(data["{}.{}".format(
                base_model.__class__.__name__, base_model.id)
                ], base_model.to_dict())


class Testreload(unittest.TestCase):

    def test_reload_no_json_format_if_file_exist(self):
        # test if reload method saves JSON format in objects if file exist
        file_path = "file.json"
        if os.path.exists(file_path):
            os.remove(file_path)
        file_storage = FileStorage()
        base_model = BaseModel()
        file_storage.save()
        file_storage.__file_path = "non_existent_file.json"
        file_storage.reload()
        self.assertIn("{}.{}".format(base_model.__class__.__name__,
                      base_model.id), file_storage.all())
        self.assertEqual(base_model.to_dict(), file_storage.all()[
            "{}.{}".format(base_model.__class__.__name__, base_model.id)
            ].to_dict())
        os.remove(file_path)


if __name__ == '__main__':
    unittest.main()
