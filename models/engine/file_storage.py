#!/usr/bin/python3
"""
    Serialization - deserialization tool
"""

import json
import os.path

from models.base_model import BaseModel


class FileStorage():
    """
        classe that serializes instances to a JSON file
        and deserializes JSON file to instances

        ATTRIBUTS:
        =============

            __file_path : private, path to the JSON file

            __objects: private, dict store all object
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
            return the dictionary __objects
        """
        return (FileStorage.__objects)

    def new(self, obj):
        """
            new entry in dict __objects
        """
        # create string for key
        field_classname = obj.__class__.__name__
        # add new key=obj in dict
        FileStorage.__objects['{}.{}'.format(field_classname, obj.id)] = obj

    def save(self):
        """
            Serialize __objects to the JSON file
        """
        obj_list = {}
        for key, value in self.__objects.items():
            obj_list[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as out_file:
            json.dump(obj_list, out_file)

    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding='utf-8') as rf:
                reload = json.load(rf)
                for k, v in reload.items():
                    v = eval(v["__class__"])(**v)
                    self.__objects[k] = v
                    self.new(v)
