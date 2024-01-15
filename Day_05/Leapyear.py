# Write a program that determines whether a given year is a leap year or not. A leap year is either divisible by 4 but not divisible by 100, or it is divisible by 400.
# Input the year from the user
year = int(input("Enter a year: "))

# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
---------------------------------------------------------------
# You can also use Calendar module 
import calendar

# Input the year from the user
year = int(input("Enter a year: "))

# Check if it's a leap year using the calendar module
if calendar.isleap(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
