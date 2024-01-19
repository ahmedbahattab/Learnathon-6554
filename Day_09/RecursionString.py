# Write a recursive function to reverse a string.
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]
str = input("Enter a string: ")
result = reverse_string(str)
print(f"{result}")
