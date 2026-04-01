7.# Polymorphism (Operator Overloading)

# Create a class ComplexNumber with real and imaginary parts.

# Overload the + operator to add two complex numbers.



class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real}+{self.imag}i"


# Example
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(4, 5)
c3 = c1 + c2
print("Sum:", c3)
