#!/usr/bin/python3
"""
This module contains a simple shell for interacting
with models for the HBNB project
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ command shell to interact with models """
    def __init__(self, completekey='tab', stdin=None, stdout=None) -> None:
        super().__init__(completekey, stdin, stdout)
        self.prompt = "(hbnb) "

    def do_quit(self, arg) -> bool:
        """ quit the shell """
        return True

    def do_EOF(self, arg) -> bool:
        """ quit the shell """
        return True

    def emptyline(self) -> None:
        """ command to execute on empty line """
        return

    def help_quit(self) -> None:
        """ help for quit command """
        print("Quit command to exit the program\n")

    def help_EOF(self) -> None:
        """ help for quit command """
        print("EOF to exit the program\n")


def parse(arg):
    "Convert arg to an argument tuple"
    return tuple(arg.split())


if __name__ == "__main__":
    HBNBCommand().cmdloop()
