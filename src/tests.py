
def f(x):
    answer = 0
     
    for i in range(1000):
        answer += 1
    
    for i in range(x):
        answer += x
        
    for i in range(x):
        for j in range(x):
            answer += 1
            answer += 1
            
    return answer

x= 100
print(f(x))