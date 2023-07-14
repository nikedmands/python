import math


class Shape:
    def __init__(self, name):
        self.name = name

    def get_area(self):
        pass

    def get_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.name = name
        self.length = length
        self.width = width

    def get_area(self):
        print("The area of " + self.name + " is: " + str((self.length * self.width)))

    def get_perimeter(self):
        print("The perimeter of " + self.name + " is: " + str((2 * (self.length + self.width))))


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.name = name
        self.radius = radius

    def get_area(self):
        print("The area of " + self.name + " is: " + str((3.14 * self.radius ** 2)))

    def get_perimeter(self):
        print("The perimeter of " + self.name + " is: " + str((2 * 3.14 * self.radius)))
