#!/usr/bin/python3
"""
    Entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import FileStorage


class HBNBCommand(cmd.Cmd):
    """ command interpreter python """

    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, arg):
        "Quit command to exit the program"
        quit()

    def do_EOF(self, arg):
        "Quit command to exit the program"
        return True

    def do_create(self, arg):
        if arg != 'BaseModel'and arg:
            print("** class doesn't exist **")
        elif not arg:
            print("** class name missing **")
        else:
            command = arg + "()"
            new_instance = eval(command)
            print(new_instance.id)
            new_instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
