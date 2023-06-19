#!/usr/bin/python3
"""
A module to  “base” of all other classes in this project.
The goal of it is to manage id attribute
 in all classes to avoid duplicating the same code.
 """
import json
import csv
import turtle


class Base:
    """
    Define the base class of all other classes

    Private Class Attributes:
        __nb_object (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the class consturctor

        Args:
        id (int): The identity of new base
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Update the class Base by adding the static method
        `def to_json_string(list_dictionaries)`.

        Args:
        list_dictionaries: is a list of dictionaries

        Return:
        If list_dictionaries is None or empty, return the string: "[]"
        Otherwise, return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"

        with open(filename, mode="w", encoding='utf-8') as jsonfile:
            if list_objs is None:
                return jsonfile.write(cls.to_json_string(None))

            attrs = []

            for element in list_objs:
                attrs.append(element.to_dictionary())

                return jsonfile.write(cls.to_json_string(attrs))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the deserialization of a JSON string.

        Args:
        json_string is a string representing a list of dictionaries

        Return:
        If json_string is None or empty, return an empty list
        Otherwise, return the list represented by json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return a class instantied from a dictionary of attributes.

        Args:
            **dictionary: Key/value pairs of attributes to initialize.
        """
        if cls.__name__ == 'Square':
            dummy = cls(3)

        if cls.__name__ == 'Rectangle':
            dummy = cls(3, 3)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Return a list of classes instantiated from a file of JSON strings.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, mode="r", encoding='utf-8') as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**dic) for dic in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs: A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            Empty list If the file does not exist
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for dic in list_dicts]
                return [cls.create(**dic) for dic in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw Rectangles and Squares using the turtle package.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#deb1af")
        turt.pensize(4)
        turt.shape("turtle")

        turt.color("#000000")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#ff0000")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
