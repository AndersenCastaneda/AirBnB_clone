#!/usr/bin/python3
"""Console Module"""
import cmd
import sys
from models import storage
from models import cls_list
import json
import re


class HBNBCommand(cmd.Cmd):
    """AirBnb Clone"""
    prompt = "(hbnb) "

    def do_all(self, line):
        """Prints all string representation of all instances based
        or not on the class name
        """
        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)

        if not match:
            l_obj = [str(value) for key, value in storage.all().items()]
            print(l_obj)
            return

        c_name = match.group(1)
        if c_name not in cls_list:
            print("** class doesn't exist **")
            return

        l_obj = [str(value) for key, value in storage.all().items()
                 if (c_name == type(value).__name__)]
        print(l_obj)

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)\
            and prints the id
        """
        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)

        if not match:
            print("** class name missing **")
            return

        c_name = match.group(1)
        if c_name not in cls_list:
            print("** class doesn't exist **")
            return

        b = storage.create()[line]()
        b.save()
        print(b.id)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        if not match:
            print("** class name missing **")
            return

        c_name = match.group(1)
        c_id = match.group(2)
        if c_name not in cls_list:
            print("** class doesn't exist **")
            return
        if c_id is None:
            print("** instance id missing **")
            return

        key = "{}.{}".format(c_name, c_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        storage.destroy(key)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = line.split(" ")
        if line in [None, ""]:
            print("** class name missing **")
        elif storage.classes(args[0]):
            print("** class doesn't exist **")
        else:
            if len(args) == 1:
                print("** instance id missing **")
                return
            else:
                key = "{}.{}".format(args[0], args[1])

            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_EOF(self, line):
        """Handles the End Of File"""
        return True

    def do_quit(self, line):
        """Exit programm"""
        return True

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file) """
        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)

        if not match:
            print("** class name missing **")
            return

        c_name = match.group(1)
        c_id = match.group(2)
        c_attribute = match.group(3)
        c_value = match.group(4)
        if storage.classes(c_name):
            print("** class doesn't exist **")
        elif c_id is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(c_name, c_id)
            if key not in storage.all():
                print("** no instance found **")
            elif c_attribute is None:
                print("** attribute name missing **")
            elif c_value is None:
                print("** value missing **")
            else:
                setattr(storage.all()[key], c_attribute, c_value)
                storage.save()

    def emptyline(self):
        """Handles empty line"""
        return

    def help_quit(self):
        """Print quit instruction"""
        print("Quit command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
