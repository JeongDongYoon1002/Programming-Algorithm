import sys
input = sys.stdin.readline 

test_case = int(input())
for i in range(test_case):
    n = int(input())
    arr = []
    while n >= 2:
        arr.append(n%2)
        n = n // 2
    if n == 1:
        arr.append(1)

    for i in range(len(arr)):
        if arr[i] == 1:
            print(i, end = ' ')
    
