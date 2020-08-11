#!/usr/bin/python3
""" test_console.py

    Test of console.py file
"""
import unittest
import console
import pep8
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import os.path as path
import os


class testConsole(unittest.TestCase):
    """TestConsole Class

    Test cases of console.py
    """

    def test_pep8_console(self):
        """test_pep8_console test

        Test pep8 for console.py file
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0)

    def test_console_prompt(self):
        """test_console_prompt

        test if prompt is correct
        """
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_console_docstrings(self):
        """test_console_docstrings

        test if docstrings exist alredy
        """
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_empty_line(self):
        """test_empty_line

        Test empty line entry
        """
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", out.getvalue().strip())

    def test_console_do_count(self):
        """test_console_do_count

        test output count for an instance
        """
        pass

    def test_console_do_create(self):
        pass

    def test_console_do_update(self):
        pass


if __name__ == "__main__":
    unittest.main()
