# math_operations.py

PI = 3.14159

def addition(x, y):
    """Function to perform addition."""
    return x + y

def subtraction(x, y):
    """Function to perform subtraction."""
    return x - y

def multiplication(x, y):
    """Function to perform multiplication."""
    return x * y

def division(x, y):
    """Function to perform division."""
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"
