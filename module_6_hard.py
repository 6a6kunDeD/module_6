import math

class Figure:
    def __init__(self, sides_count = 0):
        self.sides_count = sides_count
        self.__sides = []
        self.__color = []
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if self.__color[0] == r and self.__color[1] == g and self.__color[2] == b:
            return True
        return False

    def set_color(self, r, g, b):
        if len(self.__color) == 0:
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if side <= 0:
                return False
        return True

    def __len__(self):
        return len(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides

class Triangle(Figure):
    def __init__(self):
        super().__init__(sides_count=3)
        self.__base = 0
        self.__height = 0

    def get_square(self):
        return (self.__base * self.__hight) / 2

class Circle(Figure):
    def __init__(self, radius=0):
        super().__init__(sides_count=1)
        self.__radius = radius / 2

    def get_square(self):
        return 3.14 * (self.__radius ** 2)

    def set_radius(self, r):
        self.__radius = r

    def get_sides(self):
        return [self.__radius * 2]

class Cube(Figure):
    def __init__(self, side=1):
        super().__init__(sides_count=12)
        self.__side = side

    def get_sides(self):
        return [self.__side] * 12

    def get_volume(self):
        return self.__side ** 3

    def set_sides(self, side):
        if side <= 0:
            return
        self.__side = side

circle1 = Circle(10)
cube1 = Cube(6)

circle1.set_color(200, 200, 100)
circle1.set_sides(10)

cube1.set_color(222, 35, 130)
cube1.set_sides(6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())

cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(6)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())


