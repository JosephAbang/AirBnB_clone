#!/usr/bin/python3
"""
Module defines a class called `HBNBCommand`
`HBNBCommand` inherits from `cmd.Cmd` class
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand processor"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    do_EOF = do_quit

    def emptyline(self):
        """Called when an empty line is entered

        If the method is not overridden it
        repeats the last non empty command entered
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
