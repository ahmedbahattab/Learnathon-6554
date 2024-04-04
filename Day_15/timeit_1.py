# Implement a Python decorator called time_it that calculates and prints the execution time of a function. The decorator should be used to decorate a function of your choice.
import time
from functools import wraps

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

# Example usage:
@time_it
def my_function(n):
    # This function simply calculates the sum of numbers from 1 to n
    total = 0
    for i in range(1, n+1):
        total += i
    return total

# Call the decorated function
result = my_function(1000000)
print("Result:", result)
