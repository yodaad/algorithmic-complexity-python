# Sum rule in Big O notation is a rule that states that the sum of two functions is the maximum of the two functions.

def f(n):
    for i in range(n):
        print(i)
        
    for i in range(n):
        print(i)
        
# O(n) + O(n) = O(n + n) = O(2n) = O(n)

def f(n):
    for i in range(n):
        print(i)
        
    for i in range(n * n):
        print(i)
        
# O(n) + O(n * n) = O(n + n^2) = O(n^2)
