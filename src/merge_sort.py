"""Merge Sort Algorith is a simple sorting algorithm that divides the list in half, sorts each half and then merges the two halves. 
It's complexity is O(n log n) because it divides the list in half and sorts each half before merging them."""

import random

def merge_sort(list):
    if len(list) > 1:
        middle = len(list) // 2
        left_list = list[:middle]
        right_list = list[middle:]
    #    print(left_list, "*" * 5, right_list)
        
        # Recursive call on each half
        merge_sort(left_list)
        merge_sort(right_list)
        
        # Iterators for each half
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i += 1
            else:
                list[k] = right_list[j]
                j += 1
            k += 1
        
        while i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1
        
        while j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1

    #    print(f"Left list {left_list}, Right list {right_list}")
    #    print(list)
    #    print("-" * 25)
    
    return list 


if __name__ == "__main__":
    list_size = int(input("What size list do you want to create? "))
    
    list = [random.randint(0,100) for i in range(list_size)]
    print(list)
    print("-" * 20)
    
    ordered_list = merge_sort(list)
    print(ordered_list)