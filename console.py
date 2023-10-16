#!/usr/bin/python3
import cmd
import json
import re
import sys
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from shlex import split
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

def func1(specific_line):
    var_search = re.search(r"\{(.*?)\}", specific_line)
    num1 = re.search(r"\[(.*?)\]", specific_line)
    if var_search is None:
        if num1 is None:
            return [var_i.strip(",") for var_i in split(specific_line)]
        else:
            l = split(specific_line[:num1.span()[0]])
            ran = [var_i.strip(",") for var_i in l]
            ran.append(num1.group())
            return ran
    else:
        l = split(specific_line[:var_search.span()[0]])
        ran = [var_i.strip(",") for var_i in l]
        ran.append(var_search.group())
        return ran


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"
    dict1 = {
        "BaseModel", "User", "State", "City", "Place", "Amenity",
        "Review"
    }

    def do_quit(self, specific_line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, specific_line):
        """ methods used to exit the cmd """
        print()
        return True

    def help_quit(self):
        """ It will serve as a quit command. """
        print('Quit command to exit the program')        
    def do_help(self, specific_line):
        """overrideing method"""
        cmd.Cmd.do_help(self, specific_line)


    def help_EOF(self):
        print('EOF command to exit the program')

    def emp(self):
        """Empty specific_line."""
        pass

    def do_create(self, specific_line):

        if specific_line == "":
            print("** class name missing **")
        else:
            try:
                myclass = eval(specific_line + "()")
                myclass.save()
                print(myclass.id)
            except Exception as e:
                print("** class doesn't exist **")

    def do_show(self, specific_line):

        var_lines = func1(specific_line)
        var_objs = storage.all()
        if len(var_lines) == 0:
            print("** class name missing **")
        elif var_lines[0] not in HBNBCommand.dict1:
            print("** class doesn't exist **")
        elif len(var_lines) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(var_lines[0], var_lines[1]) not in var_objs:
            print("** no instance found **")
        else:
            print(var_objs["{}.{}".format(var_lines[0], var_lines[1])])

    def do_destroy(self, specific_line):

        no1 = shlex.split(specific_line)

        if len(no1) < 1:
            print("** class name missing **")
            return
        if no1[0] not in HBNBCommand.dict1:
            print("** class doesn't exist **")
            return
        if len(no1) < 2:
            print("** instance id missing **")
            return

        try:
            incon_dict = storage.all()  # get stores objects as dict
            del incon_dict["{}.{}".format(no1[0], no1[1])]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, specific_line):

        monv = func1(specific_line)
        if len(monv) > 0 and monv[0] not in HBNBCommand.dict1:
            print("** class doesn't exist **")
        else:
            thing = []
            for item1 in storage.all().values():
                if len(monv) > 0 and monv[0] == item1.__class__.__name__:
                    thing.append(item1.__str__())
                elif len(monv) == 0:
                    thing.append(item1.__str__())
            print(thing)

    def do_help(self, specific_line):
        """overrides help function"""
        cmd.Cmd.do_help(self, specific_line)

    def do_update(self, specific_line):

        no1 = shlex.split(specific_line)
        if len(no1) == 0:
            print("** class name missing **")
            return
        elif no1[0] not in HBNBCommand.dict1:
            print("** class doesn't exist **")
            return
        elif len(no1) == 1:
            print("** instance id missing **")
            return
        elif len(no1) == 2:
            print("** attribute name missing **")
            return
        elif len(no1) == 3:
            print("** value missing **")
            return
        variable_3 = []
        id = no1[1]

        try:
            objects_dict = storage.all()
            for key in objects_dict:
                class_name, inst_id = key.split(".")
                variable_3.append(inst_id)
                if id in variable_3:
                    obj = objects_dict[f"{class_name}.{id}"]
                    attr = no1[2]
                    value = no1[3]
                    setattr(obj, attr, value)
                    storage.save()
                    return
                print("** no instance found **")
                return
        except KeyError:
            print("** no instance found **")

    def do_count(self, specific_line):

        counter = 0
        class_name = specific_line
        var_all = storage.all()
        for key, obj in var_all.items():
            name = key.split(".")
            if name[0] == class_name:
                counter += 1
        print(counter)

    def default(self, specific_line):

        remin = re.match(r"(\w+\.\w+)(.*)", specific_line)
        list_command_args = ["lines_showing", "do_destroy"]

        if remin:
            vrg = remin.group(1)
            vrg = vrg.split(".")
            v_class_name = vrg[0]
            methdd_nam = vrg[1]
            fll_methdd_nam = "do_" + methdd_nam
            func_var = getattr(self, fll_methdd_nam)
            if fll_methdd_nam in ["func_imp", "do_count"]:
                func_var(v_class_name)
            elif fll_methdd_nam in list_command_args:
                """ get id as it is needed for this list of commands
                    if not passed only class name is passed """
                dzdcx1 = re.match(r'\(\"(.*)\"\)', remin.group(2))
                if dzdcx1:
                    id = dzdcx1.group(1)
                    func_var(f"{v_class_name} {id}")
                else:
                    func_var(f"{v_class_name}")
            elif fll_methdd_nam == "do_update":
                dzdcx1 = re.findall(r'[\w-]+', remin.group(2))
                no1 = " ".join(dzdcx1)
                func_var(f"{v_class_name} {no1}")

        else:
            return super().default(specific_line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()