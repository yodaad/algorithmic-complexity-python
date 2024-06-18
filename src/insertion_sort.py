"""Insertion Sort Algorithm is a simple sorting algorithm that builds the final sorted list one item at a time. It's complexity is O(n^2) because it has to check each 
element in the list for each element in the list. It's complexity is O(n^2) because it has to check each element in the list for each element in the list."""

import random

def insertion_sort(list):
    
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
        
        list[j + 1] = key
    
    return list


if __name__ == "__main__":
    list_size = int(input("What size list do you want to create? "))
    
    list = [random.randint(0,100) for i in range(list_size)]
    print(list)
    
    ordered_list = insertion_sort(list)
    print(ordered_list)