n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))


def binary_search(array, target, start, end):
    
    if start > end:
        return 0
    mid = (start+end) // 2

    if array[mid] == target:
        return 1

    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else :
        return binary_search(array, target, mid+1, end)
        

a.sort()
s = 0
e = n-1

for i in b:
    print(binary_search(a, i, s, e))
