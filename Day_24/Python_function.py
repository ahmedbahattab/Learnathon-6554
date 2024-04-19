def remove_duplicates_and_sort(input_list):
    # Convert the list to a set to remove duplicates
    unique_elements = set(input_list)
    # Sort the unique elements
    sorted_unique_elements = sorted(unique_elements)
    return sorted_unique_elements

# Example usage:
input_list = [3, 1, 2, 2, 4, 3, 5]
result = remove_duplicates_and_sort(input_list)
print(result)  # Output: [1, 2, 3, 4, 5]
