#!/usr/bin/python3
""" module_storage check file  """
import unittest
from models.engine.file_storage import FileStorage
import models.engine.file_storage
from models.base_model import BaseModel
import inspect
import os


class TestFileStorage(unittest.TestCase):
    """ class_check file storage  """

    def test_doc(self):
        """ test_doc(self): to Check if module and class has documents """
        self.assertIsNotNone(FileStorage.__doc__, 'no_documentfor FileStorage')
        self.assertIsNotNone(models.engine.file_storage.__doc__, 'no document')
        for name, method in inspect.getmembers(BaseModel, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no documents")

    def test_save_reload(self):
        """ all(), reload(), test save() functions """
        my_model = BaseModel()
        my_model.save()
        storage = FileStorage()
        """ Test if file is Initiated """
        self.assertTrue(os.path.exists('file.json'))

        """ load json file and test if objects are returned """
        storage.reload()
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertEqual(type(obj), BaseModel)

        """ positional args adding  """
        with self.assertRaises(TypeError):
            my_model.save('str')
        with self.assertRaises(TypeError):
            storage.reload('str')
        with self.assertRaises(TypeError):
            storage.all('str')

    def test_all_return_dict(self):
        """Check all ways that returns the dictionary __objects"""
        dikt_of_opj = FileStorage._FileStorage__objects
        self.assertIsInstance(dikt_of_opj, dict)

    def test_all_dict_of_obj(self):
        """Test if returns dikt of opj"""
        dikt_of_opj = FileStorage._FileStorage__objects
        for key, obj in dikt_of_opj.items():
            self.assertIsInstance(obj, object)

    def test_new(self):
        """puts in __opjects the opj with key <obj class name>.id"""
        new_baze = BaseModel()
        self.assertIn("BaseModel." + new_baze.id, models.storage.all().keys())

    def test_reload(self):
        """checks De-serialization the file JSON  to ___opjects dikt"""
        baze_inct = BaseModel()
        models.storage.new(baze_inct)
        models.storage.save()
        models.storage.reload()
        dikt_of_opj = FileStorage._FileStorage__objects
        self.assertIn(f"BaseModel.{baze_inct.id}", dikt_of_opj)

    def test_save(self):
        """Check serialization of ___objects to the file JSON """
        # make new obj save it and check key presence in file read
        baze_inct = BaseModel()
        models.storage.new(baze_inct)
        models.storage.save()
        text = ""
        with open("file.json", "r") as f:
            text = f.read()
            self.assertIn("BaseModel." + baze_inct.id, text)


if __name__ == "__main__":
    unittest.main()
