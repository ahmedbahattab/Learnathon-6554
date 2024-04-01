# Write a Python program to get the largest number from a list
def get_largest_number(numbers):
    if not numbers:
        return None  # return None if the list is empty
    return max(numbers)

# Example usage:
numbers_list = [10, 25, 7, 99, 42, 15]
largest_number = get_largest_number(numbers_list)
print("The largest number in the list is:", largest_number)
