# Product Rule in Big O notation is a rule that states that the product of two functions is the product of the two functions.

def f(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
            
# O(n) * O(n) = O(n * n) = O(n^2)