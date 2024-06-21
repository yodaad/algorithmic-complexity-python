# The Knapsack problem is a combinatorial optimization problem that seeks to maximize the total value of a set of items while keeping the total weight below a given limit. 
# The problem is NP-hard, but it can be solved efficiently using dynamic programming. The code below implements a solution to the Knapsack problem using dynamic programming. 
# The algorithm has a time complexity of O(nW), where n is the number of items and W is the maximum weight that the knapsack can hold.


def knapsack (knapsack_size, weight, values, n):
    
    if n == 0 or knapsack_size == 0:
        return 0
    
    if weight[n-1] > knapsack_size:
        return knapsack(knapsack_size, weight, values, n-1)
    
    return max(values[n-1] + knapsack(knapsack_size - weight[n-1], weight, values, n-1), knapsack(knapsack_size, weight, values, n-1))


if __name__ == "__main__":
    values = list(map(int, input("Enter the values of the items separated by space: ").split()))
    weight = list(map(int, input("Enter the weights of the items separated by space: ").split()))
    knapsack_size = int(input("Enter the maximum weight the knapsack can hold: "))
    n = len(values)
    
    result = knapsack(knapsack_size, weight, values, n)
    print(result)    
  
    
    