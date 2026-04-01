3.    # Encapsulation

    # Create a class Student with private attributes _name and _marks.

    # Provide getter and setter methods to access and update marks safely.

    # Prevent marks from being set to a value greater than 100.

class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if marks >= 0 and marks <=100:
            self.__marks = marks
        else:
            print("Invalid marks! Must be between 0 and 100.")


# Example
s1 = Student("Alice", 85)
print("Marks:", s1.get_marks())
s1.set_marks(95)
print("Updated Marks:", s1.get_marks())
s1.set_marks(150)  # invalid
