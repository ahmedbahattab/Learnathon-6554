import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        if radius >= 0:
            self.radius = radius
        else:
            print("Radius cannot be negative.")

    def calculate_area(self):
        return math.pi * self.radius ** 2

# Example usage:
circle = Circle(5)  # Create a circle with radius 5
print("Radius:", circle.get_radius())  # Output: Radius: 5
print("Area:", circle.calculate_area())  # Output: Area: 78.53981633974483

circle.set_radius(7)  # Set radius to 7
print("Radius:", circle.get_radius())  # Output: Radius: 7
print("Area:", circle.calculate_area())  # Output: Area: 153.93804002589985

circle.set_radius(-3)  # Attempt to set negative radius
print("Radius:", circle.get_radius())  # Output: Radius: 7 (unchanged)
print("Area:", circle.calculate_area())  # Output: Area: 153.93804002589985 (unchanged)
