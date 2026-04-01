#7. Polymorphism (Method Overriding)

# Create a base class Shape with a method area().

# Derive two classes Circle and Rectangle that override area() with their own formulas.



class Shape:
    def area(self):
        print("Area not defined")

class Circle(Shape):   
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Example
c = Circle(5)
r = Rectangle(4, 6)
print("Circle Area:", c.area())
print("Rectangle Area:", r.area())
