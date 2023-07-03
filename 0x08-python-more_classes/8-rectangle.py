#!/usr/bin/python3
"""A rectangle class module."""


class Rectangle:
    """A class that defines a rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation of the rectangle class.
        """
        self.width = width
        """Private instance attribute."""
        self.height = height
        "Private instance attribute."""
        type(self).number_of_instances += 1

    @property
    def width(self):
        """To retrieve the size of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """"To set the size of the rectangle.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """To retrieve the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """To set the height of the rectangle.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method
        that returns the ectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method
        that returns Rectangle perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Creates a new string.
        """
        new = ""
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                for i in range(self.__width):
                    new = new + str(self.print_symbol)
                new = new + "\n"
        return new[: -1]

    def __repr__(self):
        """Returns the canonical string
        representation of the object.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a medsage upon deletion
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns biggest rectangle based on area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
