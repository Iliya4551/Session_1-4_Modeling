import random

from point import Point

class PointException(Exception):
    """
    Custom exception class for Point-related errors.
    Useful for handling specific errors tied to point behavior.
    """
    pass

class ColorPoint(Point): #inheritance
    def __init__(self, x, y, color):
        """
        Initialize a ColorPoint with coordinates and a color.
        Raises a TypeError if x or y is not a number.
        :param x: x-coordinate (int or float)
        :param y: y-coordinate (int or float)
        :param color: string representing the point's color
        """
        if not isinstance(x, (int, float)):
            raise TypeError("X HAS TO BE A NUMBER")
        if not isinstance(y, (int, float)):
            raise TypeError("Y HAS TO BE A NUMBER")

        super().__init__(x, y) #this replaces the self.x and self.y
        self.color = color

    def __str__(self):
        """
        Returns a string representation of the color point.
        Format: <color: x, y>
        """
        return f"<{self.color}: {self.x}, {self.y}>"

if __name__ == "__main__":
    p = ColorPoint(1,2,"red")
    p.color = "rojo"
    p.x = 200

    print(p.distance_orig())
    print(p)

# colors = ["red", "green", "blue", "yellow", "black", "magenta", "cyan",
#           "white", "burgundy", "periwinkle", "marsala"]
# color_points = []
# for i in range(10):
#     color_points.append(
#         ColorPoint(random.randint(-10, 10),
#                    random.randint(-10, 10),
#                    random.choice(colors)))
#
# print(color_points)
# color_points.sort()
# print(color_points)
