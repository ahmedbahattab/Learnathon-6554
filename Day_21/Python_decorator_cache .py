def cache(func):
    cached_results = {}

    def wrapper(*args, **kwargs):
        # Create a unique key based on function name and input arguments
        key = (func.__name__, args, frozenset(kwargs.items()))
        
        # If the result is already cached, return it
        if key in cached_results:
            return cached_results[key]
        
        # Otherwise, compute the result and cache it
        result = func(*args, **kwargs)
        cached_results[key] = result
        return result

    return wrapper
#You can use this decorator by applying it to any function whose results you want to cache. For example:
@cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Computes and caches fibonacci(10)
print(fibonacci(10))  # Returns cached result for fibonacci(10)
print(fibonacci(5))   # Computes and caches fibonacci(5)
print(fibonacci(5))   # Returns cached result for fibonacci(5)
