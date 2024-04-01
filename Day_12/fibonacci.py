# Python Program to Print the Fibonacci sequence.
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage:
num_terms = int(input("Enter the number of terms in Fibonacci sequence: "))
fib_sequence = [fibonacci_recursive(i) for i in range(num_terms)]
print("Fibonacci sequence (recursive):", fib_sequence)
