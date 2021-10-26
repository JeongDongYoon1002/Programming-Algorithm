def binary_search(array, target, start, end):
    if start > end :
        return 0
    mid = (start + end) // 2

    if array[mid] == target: 
        return 1
    
    elif target > array[mid] :
        return binary_search(array, target, mid+1, end)
    elif target < array[mid]:
        return binary_search(array, target, start, mid-1)


A_num = int(input())
A = list(map(int,input().split()))
M_num = int(input())
M = list(map(int,input().split()))

A.sort()
for i in M:
    print(binary_search(A,i, 0, A_num-1))