# How would you write a recursive function to calculate the power of a number (e.g., x^n)?
def power(x, n):
    pow = 1
    for i in range(n):
        pow = pow * x
 
    return pow
x = 2
n = 3
print(power(x, n))
================================================
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

base = 2
exponent = 3
result = power(base, exponent)
print(f"{base}^{exponent} is:", result)
