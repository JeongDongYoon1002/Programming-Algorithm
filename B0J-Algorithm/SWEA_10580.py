t = int(input())
for i in range(1,t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    avg = sum(arr)/n
    cnt = 0
    for j in range(n):
        if arr[j] <= avg:
            cnt += 1
    print("#{} {}".format(i, cnt))
        
        
