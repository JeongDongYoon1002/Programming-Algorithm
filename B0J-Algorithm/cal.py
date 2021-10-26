import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
data = []
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
array = []
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] != 0:
            array.append((data[i][j], i, j))

s, y, x = map(int, sys.stdin.readline().split())


q = deque()
array.sort()
for arr in array:
    cost, y, x = arr
    q.append((cost, y, x, 0))


while q:
    cost, y, x, count = q.popleft()

    if count == s:
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < n:
            if data[ny][nx] == 0:
                data[ny][nx] = cost 
                count += 1
                q.append((data[ny][nx], ny, nx, count))

print(data[y-1][x-1])