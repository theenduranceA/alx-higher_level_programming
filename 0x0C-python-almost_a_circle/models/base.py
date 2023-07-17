#!/usr/bin/python3
"""Module for base class."""

import json
import csv
from os import path


class Base:
    """The class base."""
    __nb_objects = 0
    """Private class attribute."""

    def __init__(self, id=None):
        """Class constructoe."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns JSON string
        representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes the JSON string
        representation of list_objs to a file"""
        my_list = []
        filename = cls.__name__ + ".json"

        if list_objs is not None:
            for i in list_objs:
                my_list.append(i.to_dictionary())
        with open(filename, mode='w') as f:
            f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """Static method that returns list of the JSON string representation"""
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method that returns instance
        with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Class method that returns list of instances"""
        filename = cls.__name__ + ".json"
        my_list = []

        if path.isfile(filename):
            with open(filename) as f:
                list_output = cls.from_json_string(f.read())
            for e in list_output:
                my_list.append(cls.create(**e))
        return my_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Class method that serializes and saves the objects
        in CSV format to a file"""
        filename = cls.__name__ + ".csv"

        with open(filename, mode='w', newline='') as f:
            writer = csv.writer(f)
            for obj in list_objs:
                row = obj.to_csv_row()
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Class method that deserializes and returns
        a list of instances from a CSV file"""
        filename = cls.__name__ + ".csv"
        my_list = []

        if path.isfile(filename):
            with open(filename, newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    instance = cls.create_from_csv_row(row)
                    my_list.append(instance)

        return my_list
