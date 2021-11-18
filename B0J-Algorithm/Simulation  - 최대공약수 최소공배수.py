import sys
input = sys.stdin.readline 

def gcd(x,y):
    while(y):
        x, y = y, x%y
        
    return x 

def lcm(x,y):
    result = (x*y) // gcd(x,y)
    
    return result 

x, y = map(int,input().split())
print(gcd(x,y))
print(lcm(x,y))

