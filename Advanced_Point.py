from types import ClassMethodDescriptorType

from Color_Point import ColorPoint, PointException

class AdvancedPoint(ColorPoint):
    COLORS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"]
    def __int__(self, x, y, color):
        if color not in self.COLORS:
            raise TypeError(f"Invalid color, must be one of {self.COLORS}")
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x #the getter method

    @x.setter
    def x(self, value):
        self._x = value # the setter method

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    @classmethod #a method that applies to the class as a whole
    def add_color(cls, color):
        """
        Adds a new valid color for our class
        """
        cls.COLORS.append(color)

    @staticmethod #functions that have nothing to do with the perimeters of the class
    def from_tuple(coordinate, color="red"):
        """
        Creates a new point from a tuple rather than 2 individual values
        """
        x, y = coordinate
        return AdvancedPoint(x, y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 22) ** 0.5

    def distance_to_other(self, p):
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