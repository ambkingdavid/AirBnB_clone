#!/usr/bin/env python3
"""defines the entry point of the program"""

import cmd
import re
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel


def tokens(string):
    check = re.search(r'(\w+)\s+"([\w-]+)",\s+(\{.*\})', string)
    if check is not None:
        args = list(check.groups())
        return args
    else:
        string = " ".join(string.split(", "))
        pattern = re.findall(r'\"([^\",]*)\"|\'([^\",]*)\'|(\S+)', string)
        args = []
        for i in range(len(pattern)):
            args.append("".join(pattern[i]))
        return args


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    valid_classes = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review",
            ]

    def default(self, arg):
        """default behavior of the cmdloop when an invalid cmd is given"""
        commands = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update,
                "count": self.do_count
                }
        pattern = re.search(r'(\w+).(\w+)\((.*)\)', arg)
        if pattern is not None:
            args = list(pattern.groups())
            if args[1] in commands.keys():
                cmd = args[1]
                del args[1]
                arg_str = " ".join(args)
                return commands[cmd](arg_str)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit the console"""

        return True

    def do_EOF(self, arg):
        """Exit the console"""

        print("")
        return True

    def emptyline(self):
        """Do nothing"""

        pass

    def do_create(self, arg):
        """ creates a new instance of a class"""

        args = tokens(arg)
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(args[0])()
            print(new_obj.id)
            storage.save()

    def do_show(self, arg):
        """ Prints the string representation of an instance"""
        args = tokens(arg)
        objects = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in objects:
            print("** no instance found **")
        else:
            key = f"{args[0]}.{args[1]}"
            print(f"{objects[key]}")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""

        args = tokens(arg)
        objects = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in objects:
            print("** no instance found **")
        else:
            key = f"{args[0]}.{args[1]}"
            del objects[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""

        args = tokens(arg)
        objects = storage.all()
        if len(arg) == 0:
            for obj in objects.keys():
                print(objects[obj])
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif args[0] in self.valid_classes:
            for obj in objects.keys():
                if re.search(fr'^{re.escape(args[0])}', obj):
                    print(objects[obj])

    def do_update(self, arg):
        """Updates an instance based on the class name and id
           Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        args = tokens(arg)
        objects = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in objects:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4 and type(eval(args[2])) != dict:
            print("** value missing **")
        else:
            if len(args) == 3 and type(eval(args[2])) == dict:
                obj = objects[f"{args[0]}.{args[1]}"]
                arg_dict = eval(args[2])
                for k, v in arg_dict.items():
                    if k in obj.__dict__.keys():
                        value_type = type(obj.__dict__[k])
                        obj.__dict__[k] = value_type(v)
                    else:
                        obj.__dict__[k] = v
            else:
                obj = objects[f"{args[0]}.{args[1]}"]
                if args[2] in obj.__dict__.keys():
                    value_type = type(obj.__dict__[args[2]])
                    obj.__dict__[args[2]] = value_type(args[3])
                else:
                    obj.__dict__[args[2]] = args[3]
            storage.save()

    def do_count(self, arg):
        """retrieve the number of instances of a class"""

        args = tokens(arg)
        objects = storage.all()
        count = 0
        if len(args):
            for obj in objects.keys():
                if re.search(fr'^{re.escape(args[0])}', obj):
                    count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
