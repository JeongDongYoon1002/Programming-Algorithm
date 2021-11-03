n, m = map(int,input().split())
array = list(map(int,input().split()))



def binary_search(start, end, target):
    while start <= end :
        mid = (start + end) // 2
        result = 0
        for i in range(n):
            if array[i] - mid> 0:
                result += (array[i] - mid)


        if(target == result):
            return mid
        
        if target > result:
            end = mid - 1
        else:
            start = mid + 1
            

print(binary_search(0, max(array), m))
