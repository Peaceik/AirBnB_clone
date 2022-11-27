#!/usr/bin/python3
"""
This module contains a simple shell for interacting
with models for the HBNB project
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


models = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]


class HBNBCommand(cmd.Cmd):
    """ command shell to interact with models """
    def __init__(self, completekey='tab', stdin=None, stdout=None) -> None:
        super().__init__(completekey, stdin, stdout)
        self.prompt = "(hbnb) "

    def do_create(self, arg) -> None:
        """ creates a new instance of a model """
        if not arg:
            print("** class name missing **")
            return
        if arg not in models:
            print("** class doesn't exist **")
            return

        if arg == "BaseModel":
            model = BaseModel()
        elif arg == "User":
            model = User()
        elif arg == "Place":
            model = Place()
        elif arg == "State":
            model = State()
        elif arg == "City":
            model = City()
        elif arg == "Amenity":
            model = Amenity()
        elif arg == "Review":
            model = Review()
        storage.save()
        print(model.id)

    def do_show(self, arg):
        """ prints the string representation of an instance """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in models:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return

        print(objects[key])

    def do_destroy(self, arg):
        """ deletes an instance from the file storage """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in models:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        if not storage.delete(key):
            print("** no instance found **")

    def do_all(self, arg):
        """
        prints a list of all instances of a model
        based or not on the class name
        """
        if arg and arg not in models:
            print("** class doesn't exist **")
            return
        objects = storage.all()
        result = []
        if arg:
            for instance in objects.values():
                if instance.__class__.__name__ == arg:
                    result.append(str(instance))
        else:
            for instance in objects.values():
                result.append(str(instance))

        print(result)

    def do_update(self, arg):
        """ updates an instance and save it """
        args = arg.split()
        objects = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in models:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        instance = objects[key]
        value = args[3]
        if args[2] in instance.__dict__:
            attr_type = type(instance.__dict__[args[2]])
            if attr_type == int:
                value = int(args[3])
            elif attr_type == str:
                value = str(args[3])
            elif attr_type == float:
                value = float(args[3])
        instance.__dict__[args[2]] = value
        instance.save()

    def do_quit(self, arg) -> bool:
        """ quit the shell """
        return True

    def do_EOF(self, arg) -> bool:
        """ quit the shell """
        print()
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

    def help_create(self) -> None:
        """ help for quit create """
        print("creates a new instance of a model\n")

    def help_show(self) -> None:
        """ help for quit show """
        print("prints the string representation of an instance\n")

    def help_update(self) -> None:
        """ help for quit update """
        print("updates an instance and save it\n")

    def help_destroy(self) -> None:
        """ help for quit destroy """
        print("deletes an instance from the file storage\n")

    def help_all(self) -> None:
        """ help for quit all """
        print("prints a list of all instances of a model\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
