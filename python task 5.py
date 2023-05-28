from abc import ABC, abstractmethod
import math

class Shape(ABC):
     @abstractmethod
     def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def calculate_area(self):
        return 0.5 * self.base * self.height
        
myCircle=Circle(6)
print("Area of circle", myCircle.calculate_area())
myRectangle=Rectangle(6,4)
print("Area of rectangle", myRectangle.calculate_area())
myTriangle=Triangle(6,8)
print("Area of triangle", myTriangle.calculate_area())