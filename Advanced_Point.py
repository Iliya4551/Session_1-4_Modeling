
from types import ClassMethodDescriptorType

from Color_Point import ColorPoint, PointException

class AdvancedPoint(ColorPoint):
    """
    A subclass of ColorPoint that includes additional functionality:
    - Validates color input against a predefined list
    - Provides getter/setter methods for attributes
    - Adds class-level and static utility methods
    """
    COLORS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"]

    def __int__(self, x, y, color):
        """
        Incorrect constructor (probably meant to be __init__). Validates color and initializes attributes.
        :param x: x-coordinate
        :param y: y-coordinate
        :param color: must be in predefined COLORS list
        """
        if color not in self.COLORS:
            raise TypeError(f"Invalid color, must be one of {self.COLORS}")
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        """
        Getter for x-coordinate
        """
        return self._x

    @x.setter
    def x(self, value):
        """
        Setter for x-coordinate
        """
        self._x = value

    @property
    def y(self):
        """
        Getter for y-coordinate
        """
        return self._y

    @property
    def color(self):
        """
        Getter for color attribute
        """
        return self._color

    @classmethod
    def add_color(cls, color):
        """
        Adds a new valid color to the class-level COLORS list.
        :param color: string to be added to valid colors
        """
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color="red"):
        """
        Creates a new AdvancedPoint from a tuple of (x, y).
        :param coordinate: tuple of x and y coordinates
        :param color: optional color (defaults to "red")
        :return: AdvancedPoint instance
        """
        x, y = coordinate
        return AdvancedPoint(x, y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Calculates distance between two AdvancedPoint instances.
        :param p1: first point
        :param p2: second point
        :return: float distance
        """
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 22) ** 0.5

    def distance_to_other(self, p):
        """
        Calculates distance from this point to another point.
        :param p: another AdvancedPoint instance
        :return: float distance
        """
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 22) ** 0.5


AdvancedPoint.add_color("rojo")
p = AdvancedPoint(1, 2, "rojo")
print(p.x)
print(p)
print(p.distance_orig())
p2 = AdvancedPoint.from_tuple((3, 2))
print(p2)
print(AdvancedPoint.distance_2_points(p, p2))
print(p.distance_to_other(p2))
