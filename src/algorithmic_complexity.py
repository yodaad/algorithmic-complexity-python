# Algorithmic complexity is a measure of how long an algorithm will take to run. It is a function of the size of the input data.

import time
import sys

def factorial(n):
    answer = 1
    
    while n > 1:
        answer *= n
        n -= 1

    return answer

def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)

if __name__ == "__main__":
   n = 200000
   
   sys.setrecursionlimit(1500000)
   
   start = time.time()
   factorial(n)
   end = time.time()
   print("Time elapsed for factorial: ", end - start)
   
   start = time.time()
   factorial_recursive(n)
   end = time.time()
   print("Time elapsed for factorial_recursive: ", end - start)
    