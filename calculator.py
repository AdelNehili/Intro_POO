import math

class my_Calculator:

    def __init__(self,calculator_name):
        self.name = calculator_name

    def introduce_my_self(self):
        print(f"Hey my name is {self.name} and i'll help you to make some calculations! Let's gooo!")


    def add(self,a, b):
        """Add two numbers."""
        return a + b

    def subtract(self,a, b):
        """Subtract two numbers."""
        return a - b


    def multiply(self,a, b):
        """Multiply two numbers."""
        return a * b


    def divide(self,a, b):
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


    def quadratic(self,a, b, c):
        """Solve the quadratic equation ax^2 + bx + c = 0. Returns two solutions as a tuple."""
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return None  # No real solutions
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2