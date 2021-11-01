# 주어진 수를 m 번 더하여 가장 수 특정인덱스는 k 번 더할 수 잇음
# n 배열의 크기 m 숫자가 더해지는 횃수 k 연속으로 더할 수 있는 횟수 
n, m , k = map(int,input().split())

arr = list(map(int, input().split()))
arr.sort()

total = 0
i = 0 
while i < m:
    
    for j in range(k):
        if i == m :
            break
        total += arr[-1]
        i += 1

    if i == m :
        break
    total += arr[-2]
    i = i + 1

print(total)

    
    

