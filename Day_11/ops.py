# Example sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union
print("Union of set_a and set_b:", set_a.union(set_b))

# Intersection
print("Intersection of set_a and set_b:", set_a.intersection(set_b))

# Difference (elements present in set_a but not in set_b)
print("Difference of set_a and set_b:", set_a.difference(set_b))

# Symmetric Difference (elements present in either set_a or set_b, but not in both)
print("Symmetric Difference of set_a and set_b:", set_a.symmetric_difference(set_b))
