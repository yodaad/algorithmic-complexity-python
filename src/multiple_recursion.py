# Multiple Recursion in Big O notation is a rule that states that the multiple of two functions is the product of the two functions

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

# O(2^n)