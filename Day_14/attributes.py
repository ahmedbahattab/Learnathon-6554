# Write a Python class called Rectangle with attributes length and width, and methods to calculate its area and perimeter.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Example usage:
# Create a Rectangle object
rect = Rectangle(5, 4)

# Calculate and print area
print("Area:", rect.calculate_area())

# Calculate and print perimeter
print("Perimeter:", rect.calculate_perimeter())
