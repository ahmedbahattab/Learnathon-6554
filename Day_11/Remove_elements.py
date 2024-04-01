# Write a Python program to remove item(s) from a given set
# Define a set
my_set = {1, 2, 3, 4, 5}
print("my_set=",my_set)

# Remove a specific item from the set using remove() method
my_set.remove(3)

# Remove a specific item from the set using discard() method
my_set.discard(5)
# Display the updated set and the popped item
print("Updated set after removing items:", my_set)
