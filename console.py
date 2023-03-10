import cmd
#!/usr/bin/python3
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
        if not class_name:
            print("** class name missing **")
        elif:
            try:
                new_model = class_name()
            except NameError:
                print("** class doesn't exist **")
        if new_model:
            new_model.save()
            print(new_model.id)
    def do_show(self, class_name, id):
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()    
