class Shape:
    def draw(self):
        print("Drawing generic shape")

class Rectangle(Shape):
    def draw(self):
        print("Drawing rectangle")

class Circle(Shape):
    def draw(self):
        print("Drawing circle")

# Create instances of Rectangle and Circle classes
rectangle = Rectangle()
circle = Circle()

# Call the draw() method on each instance
rectangle.draw()
circle.draw()
