from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):  
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

shape_1 = Rectangle(10, 20)

print(shape_1.area())
