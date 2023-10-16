#!/usr/bin/python3
""" test console """
import unittest
import inspect
from console import HBNBCommand
import console
from unittest.mock import patch
from io import StringIO
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import json

class TestConsole(unittest.TestCase):

    def func_console(self):

        self.assertIsNotNone(HBNBCommand.__doc__, 'no docs for Base class')
        self.assertIsNotNone(console.__doc__, 'no docs for module')

    def checker_func_1(self):

        self.assertEqual(HBNBCommand().onecmd("EOF"), True)
        self.assertEqual(HBNBCommand().onecmd("quit"), True)

    def test_emp_linn(self):
        with patch("sys.stdout", new=StringIO()) as result:
            self.assertEqual("", result.getvalue())

class TestCreate(unittest.TestCase):
    def test_arg_leng(self):
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = "create"
            nom = "** class name missing **"
            HBNBCommand().onecmd(used_var)
            self.assertEqual(nom, result.getvalue().strip())

    def test_inva_classNam(self):

        with patch("sys.stdout", new=StringIO()) as result:
            used_var = "create UnknownClass"
            nom = "** class doesn't exist **"
            HBNBCommand().onecmd(used_var)  # excute command
            self.assertEqual(nom, result.getvalue().strip())

    def test_creited(self):
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = "create BaseModel"  # used_var
            HBNBCommand().onecmd(used_var)  # excute command
            number1 = result.getvalue().strip()

            variable_keyword = "BaseModel.{}".format(number1)
            used_var = "create BaseModel"
            self.assertIn(variable_keyword, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as result:
            used_var = "create User"  # used_var
            HBNBCommand().onecmd(used_var)
            number1 = result.getvalue().strip()

            variable_keyword = "User.{}".format(number1)
            used_var = "create User"
            self.assertIn(variable_keyword, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as result:
            used_var = "create Amenity"
            HBNBCommand().onecmd(used_var)
            number1 = result.getvalue().strip()

            variable_keyword = "Amenity.{}".format(number1)
            used_var = "create Amenity"
            self.assertIn(variable_keyword, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as result:
            used_var = "create State"
            HBNBCommand().onecmd(used_var)
            number1 = result.getvalue().strip()

            variable_keyword = "State.{}".format(number1)
            used_var = "create State"
            self.assertIn(variable_keyword, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as result:
            used_var = "create Place"  # used_var
            HBNBCommand().onecmd(used_var)  # excute command
            number1 = result.getvalue().strip()

            variable_keyword = "Place.{}".format(number1)
            used_var = "create Place"
            self.assertIn(variable_keyword, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as result:
            used_var = "create City"
            HBNBCommand().onecmd(used_var)
            number1 = result.getvalue().strip()

            variable_keyword = "City.{}".format(number1)
            used_var = "create City"
            self.assertIn(variable_keyword, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as result:
            used_var = "create Review"
            HBNBCommand().onecmd(used_var)
            number1 = result.getvalue().strip()

            variable_keyword = "Review.{}".format(number1)
            self.assertIn(variable_keyword, storage.all().keys())


class Exact_cla(unittest.TestCase):

    def fucn_excl(self):
        import_var = BaseModel()
        id = import_var.id
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'BaseModel.show("{id}")'
            HBNBCommand().onecmd(used_var)
            used_variable2 = f"[BaseModel] ({id}) {import_var.__dict__}"
            self.assertEqual(result.getvalue().strip(), used_variable2)

        import_var = User()
        id = import_var.id
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'User.show("{id}")'
            HBNBCommand().onecmd(used_var)
            used_variable2 = f"[User] ({id}) {import_var.__dict__}"
            self.assertEqual(result.getvalue().strip(), used_variable2)

        import_var = State()
        id = import_var.id
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'State.show("{id}")'
            HBNBCommand().onecmd(used_var)
            used_variable2 = f"[State] ({id}) {import_var.__dict__}"
            self.assertEqual(result.getvalue().strip(), used_variable2)

        import_var = City()
        id = import_var.id
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'City.show("{id}")'
            HBNBCommand().onecmd(used_var)
            used_variable2 = f"[City] ({id}) {import_var.__dict__}"
            self.assertEqual(result.getvalue().strip(), used_variable2)

        import_var = Place()
        id = import_var.id
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'Place.show("{id}")'
            HBNBCommand().onecmd(used_var)
            used_variable2 = f"[Place] ({id}) {import_var.__dict__}"
            self.assertEqual(result.getvalue().strip(), used_variable2)

        import_var = Amenity()
        id = import_var.id
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'Amenity.show("{id}")'
            HBNBCommand().onecmd(used_var)  # excute command
            used_variable2 = f"[Amenity] ({id}) {import_var.__dict__}"
            self.assertEqual(result.getvalue().strip(), used_variable2)

        import_var = Review()
        id = import_var.id
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'Review.show("{id}")'
            HBNBCommand().onecmd(used_var)  # excute command
            used_variable2 = f"[Review] ({id}) {import_var.__dict__}"
            self.assertEqual(result.getvalue().strip(), used_variable2)

    def test_errors(self):
        invalid_id = 23421123
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'BaseModel.show("{invalid_id}")'
            HBNBCommand().onecmd(used_var)
            used_variable2 = "** no instance found **"
            self.assertEqual(result.getvalue().strip(), used_variable2)
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = 'show'
            HBNBCommand().onecmd(used_var)
            used_variable2 = "** class name missing **"
            self.assertEqual(result.getvalue().strip(), used_variable2)
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = 'places.show("232342")'
            HBNBCommand().onecmd(used_var)
            used_variable2 = "** class doesn't exist **"
            self.assertEqual(result.getvalue().strip(), used_variable2)

        with patch("sys.stdout", new=StringIO()) as result:
            used_var = 'Place.show()'
            HBNBCommand().onecmd(used_var)  # excute command
            used_variable2 = "** instance id missing **"
            self.assertEqual(result.getvalue().strip(), used_variable2)


class TestCount(unittest.TestCase):
    def test_count(self):
        """ test counter function """
        counter = 0
        for key, values in storage.all().items():
            name = key.split(".")
            if name[0] == 'BaseModel':
                counter += 1
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = 'BaseModel.counter()'
            HBNBCommand().onecmd(used_var)
            self.assertEqual(result.getvalue().strip(), str(counter))

class Loadclass(unittest.TestCase):

    def func_load(self):
        import_var = BaseModel()
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = 'BaseModel.all()'
            HBNBCommand().onecmd(used_var)
            list_obj = json.loads(result.getvalue())
            for obj_var1 in list_obj:
                obj_var1 = obj_var1.split()
                self.assertEqual(obj_var1[0], "[BaseModel]")

        import_var = User()
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = 'User.all()'
            HBNBCommand().onecmd(used_var)
            list_obj = json.loads(result.getvalue())
            for obj_var1 in list_obj:
                obj_var1 = obj_var1.split()
                self.assertEqual(obj_var1[0], "[User]")

        import_var = State()
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = 'State.all()'
            HBNBCommand().onecmd(used_var)
            list_obj = json.loads(result.getvalue())
            for obj_var1 in list_obj:
                obj_var1 = obj_var1.split()
                self.assertEqual(obj_var1[0], "[State]")

        import_var = City()
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = 'City.all()'
            HBNBCommand().onecmd(used_var)
            list_obj = json.loads(result.getvalue())
            for obj_var1 in list_obj:
                obj_var1 = obj_var1.split()
                self.assertEqual(obj_var1[0], "[City]")

        import_var = Amenity()
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = 'Amenity.all()'
            HBNBCommand().onecmd(used_var)
            list_obj = json.loads(result.getvalue())
            for obj_var1 in list_obj:
                obj_var1 = obj_var1.split()
                self.assertEqual(obj_var1[0], "[Amenity]")

        import_var = Place()
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = 'Place.all()'
            HBNBCommand().onecmd(used_var)
            list_obj = json.loads(result.getvalue())
            for obj_var1 in list_obj:
                obj_var1 = obj_var1.split()
                self.assertEqual(obj_var1[0], "[Place]")

        import_var = Review()
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = 'Review.all()'
            HBNBCommand().onecmd(used_var)
            list_obj = json.loads(result.getvalue())
            for obj_var1 in list_obj:
                obj_var1 = obj_var1.split()
                self.assertEqual(obj_var1[0], "[Review]")

    def test_invalidClass(self):
        import_var = Review()
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = 'review.all()'
            HBNBCommand().onecmd(used_var)
            expout = "** class doesn't exist **"
            self.assertEqual(result.getvalue().strip(), expout)

class TestDestroy(unittest.TestCase):

    def check_valid(self):
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = 'BaseModel.destroy("232342")'
            HBNBCommand().onecmd(used_var)  # excute command
            used_variable2 = "** no instance found **"
            self.assertEqual(result.getvalue().strip(), used_variable2)

    def func_check_destroy(self):
        import_var = BaseModel()
        id = import_var.id
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = 'BaseModel.destroy("{id}")'
            HBNBCommand().onecmd(used_var)
            comman = storage.all()
            var_list1 = []
            for key, obj_var1 in comman.items():
                var_list1.append(key)
            self.assertNotIn(id, var_list1)

        import_var = User()
        id = import_var.id
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = 'User.destroy("{id}")'
            HBNBCommand().onecmd(used_var)  # excute command
            comman = storage.all()
            var_list1 = []
            for key, obj_var1 in comman.items():
                var_list1.append(key)
            self.assertNotIn(id, var_list1)

        import_var = State()
        id = import_var.id
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = 'State.destroy("{id}")'
            HBNBCommand().onecmd(used_var)  # excute command
            comman = storage.all()
            var_list1 = []
            for key, obj_var1 in comman.items():
                var_list1.append(key)
            self.assertNotIn(id, var_list1)

        import_var = City()
        id = import_var.id
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = 'City.destroy("{id}")'
            HBNBCommand().onecmd(used_var)
            comman = storage.all()
            var_list1 = []
            for key, obj_var1 in comman.items():
                var_list1.append(key)
            self.assertNotIn(id, var_list1)

        import_var = Place()
        id = import_var.id
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = 'Place.destroy("{id}")'
            HBNBCommand().onecmd(used_var)
            comman = storage.all()
            var_list1 = []
            for key, obj_var1 in comman.items():
                var_list1.append(key)
            self.assertNotIn(id, var_list1)

        import_var = Amenity()
        id = import_var.id
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = 'Amenity.destroy("{id}")'
            HBNBCommand().onecmd(used_var)  # excute command
            comman = storage.all()
            var_list1 = []
            for key, obj_var1 in comman.items():
                var_list1.append(key)
            self.assertNotIn(id, var_list1)

        import_var = Review()
        id = import_var.id
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = 'Review.destroy("{id}")'
            HBNBCommand().onecmd(used_var)  # excute command
            comman = storage.all()
            var_list1 = []
            for key, obj_var1 in comman.items():
                var_list1.append(key)
            self.assertNotIn(id, var_list1)

class TestUpdate(unittest.TestCase):
    def func_check_update(self):
        import_var = BaseModel()
        id = import_var.id
        import_var.name = "betty"
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'update BaseModel {id} name base1'
            HBNBCommand().onecmd(used_var)  # excute command
            self.assertEqual(import_var.name, "base1")

        import_var = User()
        id = import_var.id
        import_var.first_name = "betty"
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'update User {id} first_name John'
            HBNBCommand().onecmd(used_var)  # excute command
            self.assertEqual(import_var.first_name, "John")

        import_var = State()
        id = import_var.id
        import_var.name = "betty"
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'update User {id} name NYC'
            HBNBCommand().onecmd(used_var)
            self.assertEqual(import_var.name, "NYC")

        import_var = City()
        id = import_var.id
        import_var.name = "betty"
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'update User {id} name NYC'
            HBNBCommand().onecmd(used_var)
            self.assertEqual(import_var.name, "NYC")

        import_var = Place()
        id = import_var.id
        import_var.name = "betty"
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'update Place {id} name NYC'
            HBNBCommand().onecmd(used_var)
            self.assertEqual(import_var.name, "NYC")

        import_var = Amenity()
        id = import_var.id
        import_var.name = "betty"
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'update Amenity {id} name NYC'
            HBNBCommand().onecmd(used_var)
            self.assertEqual(import_var.name, "NYC")

        import_var = Review()
        id = import_var.id
        import_var.text = "betty"
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'update Place {id} text NYC'
            HBNBCommand().onecmd(used_var)
            self.assertEqual(import_var.text, "NYC")

    def test_update_errors(self):
        """ test errors for update function """
        import_var = BaseModel()
        id = import_var.id
        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'update BaseModel 123112 name base1'
            HBNBCommand().onecmd(used_var)
            expout = "** no instance found **"
            self.assertEqual(result.getvalue().strip(), expout)

        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'update BaseModel'
            HBNBCommand().onecmd(used_var)
            expout = "** instance id missing **"
            self.assertEqual(result.getvalue().strip(), expout)

        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'update base {import_var.id} name base1'
            HBNBCommand().onecmd(used_var)
            expout = "** class doesn't exist **"
            self.assertEqual(result.getvalue().strip(), expout)

        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'update'
            HBNBCommand().onecmd(used_var)
            expout = "** class name missing **"
            self.assertEqual(result.getvalue().strip(), expout)

        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'update BaseModel {import_var.id}'
            HBNBCommand().onecmd(used_var)
            expout = "** attribute name missing **"
            self.assertEqual(result.getvalue().strip(), expout)

        with patch("sys.stdout", new=StringIO()) as result:
            used_var = f'update BaseModel {import_var.id} name'
            HBNBCommand().onecmd(used_var)
            expout = "** value missing **"
            self.assertEqual(result.getvalue().strip(), expout)


if __name__ == '__main__':
    unittest.main()
