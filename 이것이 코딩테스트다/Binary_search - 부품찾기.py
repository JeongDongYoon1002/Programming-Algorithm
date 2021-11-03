def binary_search(start,end, target):
    while start <= end:
        mid = (start + end) //2 

        if array[mid] == target :
            return True
        if target > array[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return False
    
n = int(input())
array = list(map(int,input().split()))
m = int(input())
targets = list(map(int,input().split()))

array.sort()


for t in targets:
    if(binary_search(0, len(array)-1, t)):
        print('yes', end =' ')
    else:
        print('no', end=' ')

