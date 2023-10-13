#!/usr/bin/python3
"""
Module defines a class called `HBNBCommand`
`HBNBCommand` inherits from `cmd.Cmd` class
"""
import cmd
import shlex


class HBNBCommand(cmd.Cmd):
    """HBNBCommand processor"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    do_EOF = do_quit

    def emptyline(self):
        """
        Called when an empty line is entered

        If the method is not overridden it
        repeats the last non empty command entered
        """
        pass

    def postloop(self):
        print()

    def do_create(self, line):
        """
        Creates a new instance
        Saves instance to a JSON File
        Prints the id
        """

        _class = line
        if _class is None:
            print("** class name missing **")
            return
        if _class not in globals():
            print("** class doesn't exist **")
            return

        new_inst = globals()[_class]()
        new_inst.save()

        print(new_inst.id)
        return

    def do_show(self, line):
        """
        Prints the string representation of an instance
        """
        if len(line.split()) == 1:
            print("** instance id missing **")
            return

        _class = line.split()[0]
        _id = line.split()[1]

        if _class is None:
            print("** class name missing **")
            return
        if _class not in globals():
            print("** class doesn't exist **")
            return
        if _id is None:
            print("** instance id missing **")
            return

        obj_key = _class + '.' + _id
        all_objs = storage.all()

        for obj_id in all_objs.keys():
            if obj_id == obj_key:
                obj = all_objs[obj_id]
                print(obj)
                return
        print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        """

        if len(line.split()) == 0:
            print("** class name missing **")
            return

        _class = line.split()[0]
        _id = line.split()[1]

        if _class is None:
            print("** class name missing **")
            return
        if _class not in globals():
            print("** class doesn't exist **")
            return
        if _id is None:
            print("** instance id missing **")
            return

        obj_key = _class + "." + _id
        all_objs = storage.all()

        for obj_id in all_objs.copy().keys():
            if obj_id == obj_key:
                del all_objs[obj_id]
                return
        print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        """

        if line not in globals():
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)
        return

    def do_update(self, line):
        """
        Updates an instance
        """
        try:
            args = shlex.split(line)
            class_ = args[0]
            id_ = args[1]
            attr_name = args[2]
            attr_val = args[3]
        except Exception:
            class_ = None
            id_ = None
            attr_name = None
            attr_val = None
            pass

        if class_ is None:
            print("** class name missing **")
            return
        elif class_ not in globals():
            print("** class doesn't exist **")
            return
        if id_ is None:
            print("** instance id missing **")
            return

        all_objs = storage.all()
        obj_key = class_ + "." + id_
        if obj_key not in all_objs.keys():
            print("** no instance found **")
            return
        if attr_name is None:
            print("** attribute name missing **")
            return
        if attr_val is None:
            print("** value missing **")
            return

        inst = all_objs[obj_key]
        if hasattr(inst, attr_name):
            attr_type = type(getattr(inst, attr_name))
            if attr_type is str:
                setattr(inst, attr_name, str(attr_val))
            elif attr_type is int:
                setattr(inst, attr_name, int(attr_val))
            elif attr_type is float:
                setattr(inst, attr_name, float(attr_val))
        else:
            setattr(inst, attr_name, attr_val)
        inst.save()


if __name__ == '__main__':
    from models import storage
    from models.base_model import BaseModel
    from models.user import User
    from models.place import Place
    from models.state import State
    from models.city import City
    from models.amenity import Amenity
    from models.review import Review
    HBNBCommand().cmdloop()
