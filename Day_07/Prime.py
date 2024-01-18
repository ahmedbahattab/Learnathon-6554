# Write a program to check if a given number is prime. Use a for loop to iterate through possible divisors and break out of the loop if the number is found to be non-prime. 
# Get input from the user
number = int(input("Enter a number: "))
isprime = True
for i in range(2, number):
    if number % i == 0:
        isprime = False
        break
if isprime and number > 1:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
