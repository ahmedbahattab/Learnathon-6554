# Write a program that takes a number as input from the user and prints its multiplication table up to 10.
# Get input from the user
n= int(input("Enter a number: "))
print(f"Multiplication table for {n}:")
for i in range(1, 11):
    result = n * i
    print(f"{n} * {i} = {result}")
