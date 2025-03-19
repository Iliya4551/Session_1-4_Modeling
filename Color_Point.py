import random

from point import Point

class PointException(Exception):
    pass

class ColorPoint(Point): #inheritance
    def __init__(self, x, y, color):
        #Raise an exception if we try to have not a number
        if not isinstance(x, (int, float)):
            raise TypeError("X HAS TO BE A NUMBER")
        if not isinstance(y, (int, float)):
            raise TypeError("Y HAS TO BE A NUMBER")

        super().__init__(x, y) #this replaces the self.x amd self.y
        self.color = color


    def __str__(self):
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

