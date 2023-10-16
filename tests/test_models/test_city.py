#!/usr/bin/python3
# test cases for base class
import unittest
from models.base_model import BaseModel
from models.city import City
import models.base_model
import models.city
import inspect
import datetime
from time import sleep


class TestCity(unittest.TestCase):

    def setUp(self):

        self.i = City()

    def test_init_citty(self):

        self.assertEqual(type(self.i.id), str)
        self.assertEqual(type(self.i.updated_at), datetime.datetime)
        self.assertEqual(type(self.i.created_at), datetime.datetime)

    def test_dok_citty(self):

        self.assertIsNotNone(models.city.__doc__, 'no documents for module')
        for name, method in inspect.getmembers(City, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no documents")

    def test_to_dikt_citty(self):

        self.i.name = "NYC"
        dikt8 = self.i.to_dict()

        self.assertEqual(type(dikt8['name']), str)
        self.assertEqual(type(dikt8['__class__']), str)
        self.assertEqual(dikt8['__class__'], "City")
        self.assertEqual(type(dikt8['updated_at']), str)
        self.assertEqual(type(dikt8['id']), str)
        self.assertEqual(type(dikt8['created_at']), str)

        with self.assertRaises(TypeError):
            self.i.to_dict('str')

    def test_save_citty(self):

        current_uptodatedAt = self.i.updated_at
        self.i.save()
        self.assertNotEqual(current_uptodatedAt, self.i.updated_at)

        with self.assertRaises(TypeError):
            self.i.save(13)


if __name__ == '__main__':
    unittest.main()
