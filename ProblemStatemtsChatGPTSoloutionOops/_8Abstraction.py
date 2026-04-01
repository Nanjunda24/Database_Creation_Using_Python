# Abstraction

# Use abc module to create an abstract class Vehicle with an abstract method start().

# Create two subclasses Car and Bike that implement the start() method differently.


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with a key.")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a kick or button.")


# Example
v1 = Car()
v2 = Bike()
v1.start()
v2.start()
