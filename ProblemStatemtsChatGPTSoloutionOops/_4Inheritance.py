4.# Inheritance

# Create a base class Person with attributes name and age.

# Create a derived class Employee that adds attributes employee_id and salary.

# Add a method to display employee details.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.employee_id}, Salary: {self.salary}")


# Example
emp1 = Employee("Bob", 30, "E123", 50000)
emp1.display()
print("Name of parent: ",emp1.name)
