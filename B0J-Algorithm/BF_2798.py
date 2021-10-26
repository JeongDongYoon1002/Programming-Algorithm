n, m = map(int,input().split())
array = list(map(int,input().split()))
max_ = 0
temp = 0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1, n):
            temp = array[i] + array[j] + array[k] 
            if temp <= m:
                max_ = max(max_, temp)
print(max_)