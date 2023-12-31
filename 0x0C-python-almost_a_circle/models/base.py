#!/usr/bin/python3

"""
contains class called Base
"""

import json
import os
import csv


class Base:
    """
    has the following:
    Attributes:
    __init__(self, id=None):
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor that manages the id attribute
        Args:
        id (int): the id attribute
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns a json string
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        deserializes from json to string format
        """
        with open(f"{cls.__name__}.json", "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = []
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())

                string = cls.to_json_string(list_dict)

                file.write(string)

    @staticmethod
    def from_json_string(json_string):
        """
        deserializes from json format to string
        """
        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create an instance of class
        """
        if issubclass(cls, Base):
            if cls.__name__ == "Base":
                return Base(dictionary.get("id", None))

            if cls.__name__ == "Square":
                obj = cls(1)
            else:
                obj = cls(1, 1)

            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """
        function to load return a list of instances from file
        """

        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r") as file:
            json_string = file.read()

            dict_list = cls.from_json_string(json_string)

            return [cls.create(**i) for i in dict_list]
        
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes to CSV format
        """
        cls_name = cls.__name__
        filename = f"{cls_name}.csv"
        with open(filename, "w", newline="") as file:

            if list_objs is None or list_objs == []:
                file.write("[]")
                return

            if cls_name == "Rectangle":
                csv_format = ["id", "width", "height", "x", "y"]
            if cls_name == "Square":
                csv_format = ["id", "size", "x", "y"]

            writer = csv.DictWriter(file, fieldnames=csv_format)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes into csv file  """

        cls_name = cls.__name__
        filename = f"{cls_name}.csv"
        if not os.path.exists(filename):
            return []

        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            row_list = []
            for row in reader:
                if len(row) == 4:
                    obj = cls(1)
                    csv_format = ["id", "size", "x", "y"]
                else:
                    obj = cls(1, 1)
                    csv_format = ["id", "width", "height", "x", "y"]
                new_row = [int(i) for i in row]
                obj.update(**dict(zip(csv_format, new_row)))
                row_list.append(obj)
            return row_list
