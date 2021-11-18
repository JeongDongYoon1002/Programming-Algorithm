import sys
input = sys.stdin.readline 

test_case = int(input())

for i in range(test_case):
    arr = list(map(int,input().split()))
    arr.sort(reverse = True) 
    print(arr[2])
    
