# Write a program that calculates the factorial of a given number using a for loop.
n = int(input("Enter the Number: "))
s = 1
for i in range(1, n + 1):
    s = s * i
print(f"The factorial of {n} is: {s}")
