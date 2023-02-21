#!/usr/bin/python3
"""
    Entry point of the command interpreter
"""

import cmd
import shlex
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """ command interpreter python """

    prompt = '(hbnb) '

    NameOfClass = ["BaseModel()"]

    def emptyline(self):
        pass

    def do_quit(self, line):
        "Quit command to exit the program"
        quit()

    def do_EOF(self, line):
        "Quit command to exit the program"
        return True

    def do_create(self, arg):
        """
            CREATE : create an new instance of class
                     print id
                     save to file
            Usage : create <class name>
        """
        if not arg:
            print("** class name missing **")
            return
        # split line arg
        ArgLine = shlex.split(arg)
        # stock command and add () to maque command valid
        command = ArgLine[0] + "()"
        if command not in self.NameOfClass:
            print("** class doesn't exist **")
            return
        # use eval to execute string as command
        new_obj = eval(command)
        # print id object and save in file
        print(new_obj.id)
        new_obj.save()

    def do_all(self, arg):
        ArgLine = shlex.split(arg)

    def do_show(self, arg):
        ArgLine = shlex.split(arg)
        # construct key
        key = ArgLine[0] + "." + ArgLine[1]
        # load storage
        allModel = models.storage.all()
        print(allModel[key])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
