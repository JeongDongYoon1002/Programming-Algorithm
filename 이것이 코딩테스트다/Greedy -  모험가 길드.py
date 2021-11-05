import sys

input = sys.stdin.readline 
n = int(input())
array = list(map(int,input().split()))

array.sort(reverse = True)

i = 0
count = 0
while i < n:
    if array[i] <= len(array[i:]):
        count += 1
        i = i + array[i]
    else:
        break 
    

print(count)
