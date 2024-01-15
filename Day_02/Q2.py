# Q2.Write a program to calculate the total cost of items including tax

num_items = int(input("Enter the number of items: "))
cost_per_item = float(input("Enter the cost per item: $"))

# Calculate the total cost without tax
total_cost_before_tax = num_items * cost_per_item

# Assume a user-defined tax rate
tax_rate = float(input("Enter the tax rate (in percentage): "))
tax_amount = total_cost_before_tax * (tax_rate / 100)

# Calculate the total cost including tax
total_cost_after_tax = total_cost_before_tax + tax_amount

print("\nResults:")
print(f"Total cost before tax: ${total_cost_before_tax:.2f}")
print(f"Tax amount ({tax_rate}%): ${tax_amount:.2f}")
print(f"Total cost after tax: ${total_cost_after_tax:.2f}")
