#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


"""console program for the airbnb clone"""


class HBNBCommand(cmd.Cmd):
    """The command line class that inherits from Cmd class"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOf command handler to exit the command line
        Args:
            line: The entered command
        Return:
            True
        """
        return True

    def do_quit(self, line):
        """quit command handler to exit the console
        Args:
            line: The command line
        Return:
            True
        """
        return True

    def emptyline(self):
        """emptyline handler, tells the console what to do incase of emptyline
        Args:
            self: The class
        """
        pass

    def do_create(self, class_name):
        """Creates a new instance of BaseModel"""
        if class_name == "" or class_name is None:
            print("** class name missing **")
        elif class_name not in storage.classes():
            print("** class doesn't exist **")
        else:
            new_model = storage.classes()[class_name]()
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(" ")
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(" ")
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del (storage.all()[key])

    def do_all(self, class_name):
        """Prints all string representation of all instances"""
        if class_name != "" or class_name is not None:
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                print([str(value)
                       for key, value in storage.all().items()
                       if class_name == value.__class__.__name__])
        else:
            print([str(obj) for k, obj in storage.all().items()])

    def do_update(self, line):
        """Updates an instance """
        if line == "" or line is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
