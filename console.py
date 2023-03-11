#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


"""console program for the airbnb clone"""
class HBNBCommand(cmd.Cmd):
    """The command line class that inherits from Cmd class"""
    prompt="(hbnb)"
    def do_EOF(self, line):
        """EOf command handler to exit the command line
        Args:
            line: The entered command
        Return:
            True
        """
        return True
    def help_EOF(self):
        """Provides help on the usage of EOF command
        Args:
            self: Referring to the class
        """
        print("ctrl+d: \n Exits the console \n Returns True(1)")
        
    def do_quit(self, line):
        """quit command handler to exit the console
        Args:
            line: The command line
        Return:
            True
        """
        return True
    def help_quit(self):
        """provides help on quit command to exit the console
        Args:
            self: Referring to the class
        """
        print("quit: \n Exits the cons\
ole \n Returns True(1)")
    def emptyline(self):
        """emptyline handler, tells the console what to do incase of emptyline
        Args:
            self: The class
        """
        pass
    def do_create(self, class_name):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. """
        if class_name == "" or class_name is None:
            print("** class name missing **")
        elif class_name not in storage.classses():
            print("** class doesn't exist **")
        else:
            new_model = storage.classes()[class_name]
            new_model.save()
            print(new_model.id)
            
    def do_show(self, line):
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args=line.split(" ")
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
        """Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234."""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args=line.split(" ")
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
        """Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all."""
        if class_name != "" or class_name is not None:
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                print([str(value) for key, value in storage.all().items() if class_name == value.__class__.__name__])
        else:
            print([str(obj) for k,obj in storage.all().items()])

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com". update <class name> <id> <attribute name> "<attribute value>"""
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
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()                    

if __name__ == '__main__':
    HBNBCommand().cmdloop()    
