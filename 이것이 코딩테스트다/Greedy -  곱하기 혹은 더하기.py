import sys

input = sys.stdin.readline 
data = list(input())
data = data[:-1]

total = int(data[0])

for i in range(1, len(data)):
    if total == 0 or int(data[i]) == 0:
        total += int(data[i])
    else:
        total = total * int(data[i])

print(total)
