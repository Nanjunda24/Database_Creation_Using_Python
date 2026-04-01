# 1.Class & Object Basics

#  Create a class Car with attributes brand, model, and year.

#  Write methods to display the car details and check if the car is more than 10 years old.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

    def is_old(self):
        if 2025 - self.year > 10:
            print("This car is more than 10 years old.")
        else:
            print("This car is less than or equal to 10 years old.")


# Example
c1 = Car("Toyota", "Corolla", 2010)
c1.display()
c1.is_old()
