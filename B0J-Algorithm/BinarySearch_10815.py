n = int(input())
card = list(map(int, input().split()))
m = int(input())
array = list(map(int, input().split()))

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
        

card.sort()
s = 0
e = n-1

for i in array:
    print(binary_search(card, i, s, e), end=" ")