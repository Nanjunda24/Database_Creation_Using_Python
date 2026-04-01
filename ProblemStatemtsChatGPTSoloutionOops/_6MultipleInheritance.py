# 6.Multiple Inheritance

# Create a class Father with method skills() returning "gardening".

# Create a class Mother with method skills() returning "cooking".

# Create a class Child that inherits from both and overrides skills() to show "gardening, cooking, and programming".


class Father:
    def skills(self):
        return "Gardening"

class Mother:
    def skills(self):
        return "Cooking"

class Child(Father, Mother):
    def skills(self):
        return super().skills() + ", Cooking, Programming"


# Example
c = Child()
print("Child skills:", c.skills())
