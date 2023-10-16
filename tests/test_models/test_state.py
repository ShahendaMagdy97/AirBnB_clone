#!/usr/bin/python3
# test cases for base class
import unittest
from models.base_model import BaseModel
from models.state import State
import models.base_model
import models.state
import inspect
import datetime
from time import sleep


class TestState(unittest.TestCase):

    def setUp(self):

        self.e = State()

    def test_init_state(self):

        self.assertEqual(type(self.e.id), str)
        self.assertEqual(type(self.e.updated_at), datetime.datetime)
        self.assertEqual(type(self.e.created_at), datetime.datetime)

    def test_doc_statte(self):

        self.assertIsNotNone(models.state.__doc__, 'no documents for module')
        for name, method in inspect.getmembers(State, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no documents")

    def test_to_dikt_state(self):

        self.e.name = "NYC"
        dikt8 = self.e.to_dict()

        self.assertEqual(type(dikt8['name']), str)
        self.assertEqual(type(dikt8['__class__']), str)
        self.assertEqual(dikt8['__class__'], "State")
        self.assertEqual(type(dikt8['updated_at']), str)
        self.assertEqual(type(dikt8['id']), str)
        self.assertEqual(type(dikt8['created_at']), str)

        with self.assertRaises(TypeError):
            self.e.to_dict('str')

    def test_keep_statte(self):

        current_uptodatedAt = self.e.updated_at
        self.e.save()
        self.assertNotEqual(current_uptodatedAt, self.e.updated_at)

        with self.assertRaises(TypeError):
            self.e.save(13)


if __name__ == '__main__':
    unittest.main()
