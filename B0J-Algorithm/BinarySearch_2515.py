n = int(input())
m = list(map(int,input().split()))
total_m = int(input())

start, end = 1, max(m)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in m:
        if i >= mid:
            total += mid
        else:
            total += i

    if total > total_m:
        end = mid - 1
    else:
        start = mid + 1

print(end)




