#!/usr/bin/python3
"""
    Entry point of the command interpreter
"""


import cmd
import shlex
import models
import re
import os
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """ command interpreter python. """

    prompt = '(hbnb) '

    NameOfClass = ["BaseModel", "User", "City",
                   "Place", "Review", "State", "Amenity"]

    Commande = ['all', 'count', 'show', 'destroy', 'update', 'create']

    def emptyline(self):
        """ when tap return """
        pass

    def precmd(self, line):
        """
            To treat line of command before execut it
            ex : line : <class>.command(<id>, <attribute name>,
                        <attribute value>)
                    isolate <class>, command, <id>, <attribute name>
                    and <attribute value>
                    rebuildt line to send as line of command
        """
        classe = ''
        commande = ''
        if '.' not in line:
            return (line)
        try:
            # try parse line
            lineSplit = line[:]
            # isolate class
            classe = lineSplit[0:lineSplit.find('.')]
            # isolate cmd
            cmd = lineSplit[lineSplit.find('.') + 1:lineSplit.find('(')]
            if cmd not in HBNBCommand.Commande:
                raise Exception
            # isolate id
            id_ = lineSplit[lineSplit.find('(')+1: lineSplit.find(',')]
            # isolate args
            args_split = lineSplit[lineSplit.find(
                ',') + 3: lineSplit.find(')')]
            # isolate name attribut
            name_attb = args_split[:args_split.find('\"')]
            # isolate attribute value
            value_attb = args_split[args_split.find(',') + 3:-1]
            line = "{} {} {} {} '{}'".format(
                cmd, classe, id_, name_attb, value_attb)
        except Exception as e:
            print(e)
        finally:
            return (line)

    def do_quit(self, line):
        """ Quit command to exit the program """
        quit()

    def do_EOF(self, line):
        """ Quit command to exit the program """
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
        if ArgLine[0] not in self.NameOfClass:
            print("** class doesn't exist **")
            return
        # use eval to execute string as command
        new_obj = eval(command)
        # print id object and save in file
        print(new_obj.id)
        new_obj.save()

    def do_show(self, arg):
        """
            SHOW : Show element corresponding of class name and id
            Usage : show <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return
        ArgLine = shlex.split(arg)
        if ArgLine[0] not in self.NameOfClass:
            print("** class doesn't exist **")
            return
        if len(ArgLine) < 2:
            print("** instance id missing **")
            return
        # construct key
        key = ArgLine[0] + "." + ArgLine[1]
        # load storage
        allModel = models.storage.all()
        if key in allModel:
            print(allModel[key])
        else:
            print("** no instance found **")
            return

    def do_destroy(self, arg):
        """
            DESTROY : delete instance based on the class name an id
            Usage : destroy <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return
        ArgLine = shlex.split(arg)
        if ArgLine[0] not in self.NameOfClass:
            print("** class doesn't exist **")
            return
        if len(ArgLine) < 2:
            print("** instance id missing **")
            return
        key = ArgLine[0] + "." + ArgLine[1]
        if key in models.storage.all():
            # load list of object and suppress key element
            models.storage.all().pop(key)
            # save modification
            models.storage.save()
        else:
            print("** no instance found **")
            return

    def do_all(self, arg):
        """
            ALL : Prints all string representation of all instances based or
                  not on the class name
            Usage : all
                    all <class name>
                    <class name>.all()
        """
        ArgLine = shlex.split(arg)
        allModel = models.storage.all()
        list_obj = []
        if not arg:
            for obj_key in allModel.keys():
                obj = allModel[obj_key]
                # create list with each obj as string
                list_obj.append(str(obj))
            print(list_obj)
        else:
            if len(ArgLine) > 0 and ArgLine[0] not in self.NameOfClass:
                print("** class doesn't exist **")
            else:
                # ArgLine[0] = class of object
                obj_key = ArgLine[0]
                for k, v in allModel.items():
                    # in list object, split class_name.id to isolate class name
                    k_split = k.split(".")
                    # test if object is type class_name
                    if k_split[0] == obj_key:
                        obj = allModel[k]
                        # create liste of obj as string
                        list_obj.append(str(obj))
                        print(str(list_obj))

    def do_update(self, arg):
        """
            UPDATE : Updates an instance based on the class name
                     and id by adding or updating attribute
           Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        ArgLine = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return
        if len(ArgLine) == 1:
            print("** instance id missing **")
            return
        if len(ArgLine) == 2:
            print("** attribute name missing **")
            return
        if len(ArgLine) == 3:
            print("** value missing **")
            return
        if len(ArgLine) >= 4:
            if ArgLine[0] not in self.NameOfClass:
                print("** class doesn't exist **")
                return
            key = str(ArgLine[0]) + '.' + str(ArgLine[1])
            # load storage
            allModel = models.storage.all()
            if key not in allModel:
                print("** no instance found **")
            else:
                # store corresponding instance
                v = allModel[key]
                # use dict to append dictionary
                v.__dict__[ArgLine[2]] = ArgLine[3]
                # save change
                models.storage.all()[key].save()

    def do_count(self, arg):
        """
            COUNT: retrieve the number of instances of a class
            Usage : <class name>.count()
        """
        count_obj = 0
        for key in models.storage.all().keys():
            key = key.split('.')[0]
            if key == arg:
                count_obj += 1
        print(count_obj)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
