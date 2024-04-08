class Shape:
    def draw(self):
        print("Shape is being drawn.")

class Rectangle(Shape):
    def draw(self):
        print("Rectangle is being drawn.")

class Circle(Shape):
    def draw(self):
        print("Circle is being drawn.")

# Creating instances of Rectangle and Circle
rectangle = Rectangle()
circle = Circle()

# Calling the draw() method for each shape
rectangle.draw()
circle.draw()
