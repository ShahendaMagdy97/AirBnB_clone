#!/usr/bin/python3

import json
import os
from datetime import datetime
from models.review import Review
from models.user import User
from models.place import Place
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.amenity import Amenity


class FileStorage:

    __file_path = "./file.json"
    __objects = {}

    def new(self, obj):

        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def all(self):

        return self.__objects

    def reload(self):
        zizt3 = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                zizt3 = json.loads(f.read())

        keys = list(zizt3.keys())
        q = 0

        while q < len(keys):
            key = keys[q]
            obj_dict = zizt3[key]
            cls = globals()[obj_dict['__class__']]
            self.__objects[key] = cls(**obj_dict)
            q += 1

    def save(self):
        to_json = ""
        zizt3 = {}

        keys = list(self.__objects.keys())
        q = 0

        while q < len(keys):
            key = keys[q]
            value = self.__objects[key].to_dict()
            zizt3[key] = value
            q += 1

        to_json = json.dumps(zizt3)

        with open(self.__file_path, "w") as f:
            f.write(to_json)
