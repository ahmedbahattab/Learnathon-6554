'''`cmath` is a Python module that provides mathematical functions for complex numbers.
- `cmath.sqrt(x)`: Returns the square root of a complex number.
In the context of the quadratic equation example, `cmath.sqrt` is used to calculate the square root of a complex number, allowing the program to handle cases where the discriminant is negative (imaginary roots)'''
import cmath

# Input coefficients from the user
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the discriminant
discriminant = cmath.sqrt(b**2 - 4*a*c)

# Calculate the solutions
root1 = (-b + discriminant) / (2*a)
root2 = (-b - discriminant) / (2*a)

# Print the results
print(f"The solutions for the quadratic equation {a}x^2 + {b}x + {c} = 0 are:")
print(f"Root 1: {root1:.2f}")
print(f"Root 2: {root2:.2f}")
