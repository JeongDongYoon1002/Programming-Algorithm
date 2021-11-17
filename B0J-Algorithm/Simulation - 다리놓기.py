def combination(a, b):
    result = 1
    index = 0

    while index <= b - 1:
        result = result * a 
        a -= 1
        index += 1  
    return result

def factorial(num):
    result = 1
    for i in range(num, 0, -1):
        result = result * i
    return result

test_case = int(input())
for _ in range(test_case):
    a, b = map(int,input().split())
    result = combination(b,a) / factorial(a)
    
    print(int(result))
    
    
    
    
