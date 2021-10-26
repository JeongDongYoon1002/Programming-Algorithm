import bisect
'''
n = int(input())
arr = list(map(int,input().split()))

dp = [arr[0]]

for i in range(n):
    
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp,arr[i])
        dp[idx] = arr[i]

print(len(dp))
'''

nums = [0,1,2,3,4,5,6,7,8,9] 
n = 15
print(bisect.bisect_left(nums, n)) 
print(bisect.bisect_right(nums, n))

