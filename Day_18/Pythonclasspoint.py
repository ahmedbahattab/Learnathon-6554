class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type(s) for +: '{}' and '{}'".format(type(self), type(other)))

# Demonstration
point1 = Point(3, 4)
point2 = Point(1, 2)
result = point1 + point2
print("Resulting point after addition: ({}, {})".format(result.x, result.y))
