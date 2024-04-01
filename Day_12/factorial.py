# Python Program to Find the Factorial of a Number
def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

# Example usage:
num = int(input("Enter a number: "))
print("Factorial of", num, "is:", factorial_iterative(num))
