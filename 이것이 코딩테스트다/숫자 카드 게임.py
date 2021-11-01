n, m = map(int, input().split()) #n 세로 m 가로 
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

min_value = -1

for i in range(n):
    min_value = max(min_value, min(arr[i]))

print(min_value)
