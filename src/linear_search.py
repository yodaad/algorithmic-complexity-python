"""Linear Search Algorithm is a searching algorithm that finds the position of a target value within a list. 
It sequentially checks each element of the list until a match is found or the whole list has been searched. If the target value is not in the list, the search algorithm will return False. 
It's complexity is O(n) because it has to check each element in the list"""

import random

def linear_search(list, target):
    match = False
    
    for element in list:
        if element == target:
            match = True
            break
        
    return match

if __name__ == "__main__":
    list_size = int(input("What size list do you want to create? "))
    target = int(input("What numnber are you looking for? "))
    
    list = [random.randint(0,100) for i in range(list_size)]
    
    print(list)
    print(f"The element {target} {"is" if linear_search(list, target) else "is not" } in the list")