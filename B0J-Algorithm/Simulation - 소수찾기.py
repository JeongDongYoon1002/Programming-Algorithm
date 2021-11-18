import sys
input = sys.stdin.readline 
def find(num):
    for i in range(2, num):
        if num % i == 0 :
            return False 
    return True
 
n = int(input())
arr = list(map(int,input().split()))
result = 0

for i in range(len(arr)):
    if find(arr[i]) and arr[i] > 1:
        result += 1
        
print(result)
    
