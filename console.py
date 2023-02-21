#!/usr/bin/python3
"""
    Entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ command interpreter python """

    prompt = '(hbnb)'

    def emptyline(self):
        pass

    def do_quit(self, line):
        "Quit command to exit the program"
        quit()

    def do_EOF(self, line):
        "Quit command to exit the program"
        return True

    def help(self, arg):
        if arg == 'quit':
            print('\n'.join("Quit command to exit the program"))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
