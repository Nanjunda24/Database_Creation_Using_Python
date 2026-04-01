5.# Multilevel Inheritance

# Create a class Animal with a method sound().

# Create a class Mammal that inherits from Animal.

# Create a class Dog that inherits from Mammal and overrides the sound() method to print "Bark".


class Animal:
    def sound(self):
        print("Animal makes a sound")

class Mammal(Animal):
    def sound(self):
        print("Mammal makes a sound")

class Dog(Mammal):
    def sound(self):
        print("Dog Bark")


# Example
d = Dog()
d.sound()
