#!/usr/bin/python3
"""
base model Unittest
"""
import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestConstructor(unittest.TestCase):
    """ check class for the max_integar() function.
    """
    user = User()
    user.email = "Alx@Alx.com"
    user.password = "EL0mda"
    user.first_name = "Alx"
    user.last_name = "Said"

    def test_create_instance_without_kwargs(self):

        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user, BaseModel)
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
        self.assertEqual(self.user.email, "Alx@Alx.com")
        self.assertEqual(self.user.password, "EL0mda")
        self.assertEqual(self.user.first_name, "Alx")
        self.assertEqual(self.user.last_name, "Said")

    def test_preknown_values(self):
        """check default value"""

        t = User()
        self.assertEqual(t.email, "")
        self.assertEqual(t.password, "")
        self.assertEqual(t.first_name, "")
        self.assertEqual(t.last_name, "")

    def test_to_dict(self):

        to_dict_returned_dict = self.user.to_dict()
        expected_dict = self.user.__dict__.copy()
        expected_dict["__class__"] = self.user.__class__.__name__
        expected_dict["updated_at"] = self.user.updated_at.isoformat()
        expected_dict["created_at"] = self.user.created_at.isoformat()
        self.assertDictEqual(expected_dict, to_dict_returned_dict)

    def test_create_instance_with_kwargs(self):

        user_data = {
            "id": "user-123",
            "email": "Mo@Alx.com",
            "password": "new_password",
            "first_name": "Mo",
            "last_name": "Said",
            "created_at": "2023-08-11T23:00:25.886465",
            "updated_at": "2023-08-11T23:00:25.886466"
        }

        new_user = User(**user_data)

        self.assertIsInstance(new_user, User)
        self.assertIsInstance(new_user, BaseModel)
        self.assertIsInstance(new_user.id, str)
        self.assertIsInstance(new_user.created_at, datetime)
        self.assertIsInstance(new_user.updated_at, datetime)
        self.assertIsInstance(new_user.email, str)
        self.assertIsInstance(new_user.password, str)
        self.assertIsInstance(new_user.first_name, str)
        self.assertIsInstance(new_user.last_name, str)

        self.assertEqual(new_user.id, "user-123")
        self.assertEqual(new_user.email, "Mo@Alx.com")
        self.assertEqual(new_user.password, "new_password")
        self.assertEqual(new_user.first_name, "Mo")
        self.assertEqual(new_user.last_name, "Said")

    def test_str(self):

        m = self.user.__class__.__name__
        expected_str = f"[{m}] ({self.user.id}) <{self.user.__dict__}>"
        self.assertEqual(self.user.__str__(), expected_str)

    def test_save(self):

        before_update_time = self.user.updated_at
        self.user.email = "updated@example.com"
        self.user.save()
        after_update_time = self.user.updated_at
        self.assertNotEqual(before_update_time, after_update_time)
