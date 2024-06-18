"""Bubble Sort Algorith is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. 
The pass through the list is repeated until the list is sorted. It's complexity is O(n^2) because it has to check each element in the list for each element in the list"""

import random

def bubble_sort(list):
    n = len(list)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

if __name__ == "__main__":
    list_size = int(input("What size list do you want to create? "))
    
    list = [random.randint(0,100) for i in range(list_size)]
    print(list)
    
    ordered_list = bubble_sort(list)
    print(ordered_list)


