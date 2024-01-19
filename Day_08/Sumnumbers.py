# Write a function called sum_numbers that takes two numbers as arguments and returns their sum
def sum_numbers(num1, num2):
    return num1 + num2
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
result = sum_numbers(number1, number2)
print(f"The sum of {number1} and {number2} is: {result}")
