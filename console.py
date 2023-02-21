#!/usr/bin/python3
"""
    Entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ command interpreter python """
    
    def quit(self, line):
        quit()



    def EOF(self, line):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
