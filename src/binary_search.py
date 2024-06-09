"""Binary Search Algorithm in Python is a searching algorithm that finds the position of a target value within a list. It compares the target value to the middle element of the list. 
If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the 
target value, and repeating this until the target value is found. If the search ends with the remaining half being empty, the target is not in the list. 
It's complexity is O(log n) because it divides the list in half each time it searches for the target value."""

import random

def binary_search(list, start, end, target):
    print(f"Looking for {target} in between {list[start]} and {list[end-1]}")
    if start >= end:
        return False
    
    mid = (start + end) // 2
    
    if list[mid] == target:
        return True
    elif list[mid] < target:
        return binary_search(list, mid + 1, end, target)
    else:
        return binary_search(list, start, mid - 1, target)
    
  
if __name__ == "__main__":
    list_size = int(input("What size list do you want to create? "))
    target = int(input("What number are you looking for? "))
    
    list = sorted([random.randint(0,100) for i in range(list_size)])
    
    found = binary_search(list, 0, len(list), target)
    
    print(list)
    print(f"The element {target} {"is" if found else "is not" } in the list")